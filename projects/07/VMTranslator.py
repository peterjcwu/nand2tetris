import os
import re
import logging
from abc import ABC
from typing import List
_label_counter = 0
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class VMRowBase(ABC):
    MATCH_RE = re.compile(r".*")

    def __init__(self, translator):
        self.line: str = ""
        self.lno: int = 0
        self.file_name = translator.file_name

    def _get_arg(self, i: int) -> str:
        return self.line.split(" ")[i]

    def update(self, line: str, lno: int):
        self.line = line
        self.lno = lno

    def match(self) -> bool:
        return self.MATCH_RE.match(self.line) is not None

    def check(self):
        pass

    def to_asm(self) -> List[str]:
        return []

    @staticmethod
    def get_label(name: str):
        global _label_counter
        label = f"{name}.{'{:0>4}'.format(_label_counter)}"
        _label_counter += 1
        return label

    @property
    def comparison_pre(self) -> List[str]:
        return [
            '@SP',
            'AM=M-1',
            'D=M',
            'A=A-1',
            'D=M-D',  # stack[1] - stack[0]
        ]

    @staticmethod
    def comparison(jump_type: str, pass_label: str, after_label: str):
        return [
            f'@{pass_label}',
            jump_type,  # false
            '@SP',
            'A=M-1',
            'M=0',  # 0 for false
            f'@{after_label}',
            '0;JMP',
            f'({pass_label})',
            '@SP',
            'A=M-1',
            'M=-1',  # -1 for true
            f'({after_label})',
        ]

    @staticmethod
    def push_name(name: str) -> List[str]:
        return [
            f"@{name}",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
            "",
        ]

    @staticmethod
    def pop() -> List[str]:
        return [
            '@SP',
            'M=M-1',  # point to top of stack
            'A=M',
            'D=M',  # pop in D
        ]

    @staticmethod
    def push() -> List[str]:
        return [
            '@SP',
            'A=M',
            'M=D',  # * SP = D
            '@SP',
            'M=M+1',
        ]

    @classmethod
    def push_names(cls, names: List[str]) -> List[str]:
        res = []
        for n in names:
            res.extend(cls.push_name(n))
        return res

    @staticmethod
    def bootstrap() -> List[str]:
        return [
            "// -- bootstrap --",
            "@256",
            "D=A",
            "@SP",
            "M=D",
            "",
        ]


class VMRowAdd(VMRowBase):
    MATCH_RE = re.compile(r"^add", re.I)

    def to_asm(self) -> List[str]:
        return [
            f"// -- add --",
            '@SP',
            'AM=M-1',
            'D=M',
            'A=A-1',
            'D=D+M',
            'M=D',
            ""
        ]


class VMRowSub(VMRowBase):
    MATCH_RE = re.compile(r"sub", re.I)

    def to_asm(self) -> List[str]:
        return [
            '// -- sub --',
            '@SP',
            'AM=M-1',
            'D=M',
            'A=A-1',
            'D=M-D',
            'M=D',
            '',
        ]


class VMRowNeg(VMRowBase):
    MATCH_RE = re.compile(r"neg", re.I)

    def to_asm(self) -> List[str]:
        return [
            '// -- neg --',
            '@SP',
            'A=M-1',
            'M=-M',
            ''
        ]


class VMRowEq(VMRowBase):
    MATCH_RE = re.compile(r"^eq", re.I)

    def to_asm(self) -> List[str]:
        return [
            '// -- eq -- ',
            *self.comparison_pre,
            *self.comparison('D;JEQ', self.get_label("eq.pass"), self.get_label("eq.after")),
            '',
        ]


class VMRowGt(VMRowBase):
    MATCH_RE = re.compile(r"^gt", re.I)

    def to_asm(self) -> List[str]:
        return [
            '// -- greater than -- ',
            *self.comparison_pre,
            *self.comparison('D;JGT', self.get_label("gt.pass"), self.get_label("gt.after")),
            "",
        ]


class VMRowLt(VMRowBase):
    MATCH_RE = re.compile(r"^lt", re.I)

    def to_asm(self) -> List[str]:
        return [
            '// -- less than -- ',
            *self.comparison_pre,
            *self.comparison('D;JLT', self.get_label("lt.pass"), self.get_label("lt.after")),
            "",
        ]


class VMRowAnd(VMRowBase):
    MATCH_RE = re.compile(r"^and", re.I)

    def to_asm(self) -> List[str]:
        return [
            '// -- and --',
            '@SP',
            'AM=M-1',
            'D=M',
            'A=A-1',
            'M=D&M',
            '',
        ]


class VMRowOr(VMRowBase):
    MATCH_RE = re.compile(r"^or", re.I)

    def to_asm(self) -> List[str]:
        return [
            '// -- or --',
            '@SP',
            'AM=M-1',
            'D=M',
            'A=A-1',
            'M=D|M',
            ''
        ]


class VMRowNot(VMRowBase):
    MATCH_RE = re.compile(r"^not", re.I)

    def to_asm(self) -> List[str]:
        return [
            '// -- not --',
            '@SP',
            'A=M-1',
            'M=!M',
        ]


class VMRowPush(VMRowBase):
    MATCH_RE = re.compile("^push", re.I)

    def __init__(self, vm_translator):
        VMRowBase.__init__(self, vm_translator)
        self.var_type: str = ""
        self.val: int = 0
        self.RESERVED_LOC = {
            "argument": "ARG",
            "local": "LCL",
            "this": "THIS",
            "that": "THAT",
        }

    def update(self, line: str, lno: int):
        self.line = line
        self.lno = lno
        tokens = [t for t in line.split(" ") if t.strip() != ""]
        if len(tokens) == 3:
            self.var_type = tokens[1]
            self.val = int(tokens[2])

    def to_asm(self) -> List[str]:
        if self.var_type == "constant":
            return self.to_asm_constant()

        elif self.var_type == "pointer":  # r3-r4
            assert self.val <= 1, f"Pointer value can not exceed 1 at line {self.lno}"
            return self.to_asm_offset_push(3)

        elif self.var_type == "temp":  # r5-r12
            assert self.val <= 7, f"Temp value cannot exceed 7 at line {self.lno}"
            return self.to_asm_offset_push(5)

        elif self.var_type == "static":  # r16-r255
            return self.to_asm_static_push()

        else:
            return self.to_asm_name_push()

    def to_asm_constant(self) -> List[str]:
        return [
            f"// -- {self.line} --",
            f"@{self.val}",
            "D=A",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
            ""
        ]

    def to_asm_static_push(self) -> List[str]:
        return [
            f"// -- {self.line} --",
            f"@{self.file_name}.{self.val}",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
            ""
        ]

    def to_asm_offset_push(self, base_val: int) -> List[str]:
        return [
            f"// -- {self.line} --",
            f"@{self.val + base_val}",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
        ]

    def to_asm_name_push(self) -> List[str]:
        return [
            f"// -- {self.line} --",
            f"@{self.RESERVED_LOC[self.var_type]}",
            "D=M",
            f"@{self.val}",
            "D=D+A",
            "A=D",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
        ]


class VMRowPop(VMRowPush):
    MATCH_RE = re.compile(r"^pop", re.I)

    def to_asm(self) -> List[str]:
        if self.var_type == "pointer":
            assert self.val <= 1
            return self.to_asm_offset_pop(3)
        elif self.var_type == "temp":
            assert self.val <= 7
            return self.to_asm_offset_pop(5)
        elif self.var_type == "static":
            return self.to_asm_static_pop()
        else:
            return self.to_asm_name_pop()

    def to_asm_offset_pop(self, base_val: int) -> List[str]:
        return [
            f"// -- {self.line} --",
            f"@{self.val + base_val}",
            "D=A",
            "@14",
            "M=D",
        ] + self._footer

    def to_asm_name_pop(self) -> List[str]:
        return [
            f"// -- {self.line} --",
            f"@{self.RESERVED_LOC[self.var_type]}",
            "D=M",
            f"@{self.val}",
            "D=D+A",
            "@14",
            "M=D",
        ] + self._footer

    @property
    def _footer(self) -> List[str]:
        return [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@14",
            "A=M",
            "M=D",
            ""
        ]

    def to_asm_static_pop(self) -> List[str]:
        return [
            f"// -- {self.line} --",
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            f"@{self.file_name}.{self.val}",
            "M=D",
            ""
        ]


class VMRowLabel(VMRowBase):
    MATCH_RE = re.compile("label", re.I)

    def to_asm(self) -> List[str]:
        return[
            f"// -- {self.line} -- ",
            f"({self._get_arg(1)})",
            ""
        ]


class VMRowGoTo(VMRowBase):
    MATCH_RE = re.compile(r"^goto", re.I)

    def to_asm(self) -> List[str]:
        return [
            f"// -- {self.line} --",
            f"@{self._get_arg(1)}",
            "0;JMP"
            "",
        ]


class VMRowIf(VMRowBase):
    MATCH_RE = re.compile(r"^if", re.I)

    def to_asm(self) -> List[str]:
        return [
            f"// -- {self.line} --",
            "@SP",
            "AM=M-1",
            "D=M",
            f"@{self._get_arg(1)}",
            "D;JNE",
            "",
        ]


class VMRowFunction(VMRowBase):
    MATCH_RE = re.compile(r"^function",  re.I)

    def to_asm(self) -> List[str]:
        return [f"// -- {self.line} --", f"({self._get_arg(1)})"] + \
               [
                   "@SP",
                   "A=M",
                   "M=0",
                   "@SP",
                   "M=M+1",  # push 0
               ] * int(self._get_arg(2)) + \
               [""]


class VMRowReturn(VMRowBase):
    MATCH_RE = re.compile(r"return", re.I)

    def to_asm(self) -> List[str]:
        END_FRAME: str = 'R13'
        RETURN_ADDR: str = 'R14'

        def save_var_from_frame(target, offset) -> List[str]:
            return [
                f"@{END_FRAME}",
                "D=M",
                f"@{offset}",
                'A=D-A',
                'D=M',
                f"@{target}",
                "M=D",
            ]

        return [
            f"// -- return --",
            "@LCL",
            "D=M",
            f"@{END_FRAME}",
            "M=D",  # END_FRAME = LCL"
            *save_var_from_frame(RETURN_ADDR, 5),
            *self.pop(),

            "@ARG",
            "A=M",
            "M=D",  # *ARG = *SP

            "@ARG",
            "D=M+1",
            "@SP",
            "M=D",  # SP = ARG + 1

            *save_var_from_frame('THAT', 1),
            *save_var_from_frame('THIS', 2),
            *save_var_from_frame('ARG', 3),
            *save_var_from_frame('LCL', 4),

            f"@{RETURN_ADDR}",
            "A=M",
            "0;JMP",  # goto RET
        ]

    
class VMRowCall(VMRowBase):
    MATCH_RE = re.compile(r"^call", re.I)
    
    def to_asm(self) -> List[str]:
        function_name = self._get_arg(1)
        n_args = int(self._get_arg(2))
        FRAME_SIZE = 5
        RETURN_LABEL = f"{function_name}$ret.{self.lno}"

        def push_val(addr) -> List[str]:
            return [
                f'@{addr}',
                ('D=M' if re.search(r"LCL|ARG|THIS|THAT", addr, re.I) else 'D=A'),
                *self.push()]

        return [
            f"// -- {self.line} --",
            *push_val(RETURN_LABEL),
            *push_val("LCL"),
            *push_val("ARG"),
            *push_val("THIS"),
            *push_val("THAT"),
            f"@{FRAME_SIZE + n_args}",
            "D=A",
            "@SP",  # ARG = SP - (n + 5)
            "D=M-D",
            "@ARG",
            "M=D",

            "@SP",  # LCL = SP
            "D=M",
            "@LCL",
            "M=D",

            f"@{function_name}",  # goto f
            "0;JMP",
            f"({RETURN_LABEL})",
            "",
        ]


class VMTranslater:
    def __init__(self, src: str):
        # read
        self.src = os.path.abspath(src)
        self._asm_rows: List[str] = []
        self._vm_row_types: List[VMRowBase] = [
            VMRowSub(self),
            VMRowNeg(self),
            VMRowAdd(self),
            VMRowEq(self),
            VMRowGt(self),
            VMRowLt(self),
            VMRowAnd(self),
            VMRowOr(self),
            VMRowNot(self),
            VMRowPop(self),
            VMRowPush(self),
            VMRowLabel(self),
            VMRowGoTo(self),
            VMRowIf(self),
            VMRowFunction(self),
            VMRowCall(self),
            VMRowReturn(self),
        ]

        self._read()

        if os.path.exists(self.dst):
            os.unlink(self.dst)  # clean previous output

    @property
    def file_name(self) -> str:
        return os.path.basename(self.src).split(".")[0]

    @property
    def dst(self) -> str:
        if os.path.isfile(self.src):
            return re.sub(r"\.vm$", ".asm", self.src)
        else:  # self.src is dir
            return os.path.join(self.src, os.path.basename(self.src) + ".asm")

    def _read(self):
        if os.path.isfile(self.src):
            self._read_one(self.src)
            return
        vm_count = 0
        for f in os.listdir(self.src):
            if f.endswith(".vm"):
                vm_count += 1
                self._read_one(os.path.join(self.src, f))
        if vm_count > 1:
            self.push_first_bootstrap()

    def _read_one(self, src):
        with open(src, "r") as f_in:
            for i, line in enumerate(f_in.readlines()):
                line = re.sub("//.*", "", line).strip()
                if not line:
                    continue
                for vm_row_type in self._vm_row_types:
                    vm_row_type.update(line, i + 1)
                    if vm_row_type.match():
                        self._asm_rows.extend(vm_row_type.to_asm())
                        break
                else:
                    raise Exception(f"op not found on line {i}: {line}")

    def write(self):
        with open(self.dst, "w+", newline="") as f_out:
            for asm_row in self._asm_rows:
                f_out.write(asm_row + os.linesep)

    def push_first_bootstrap(self):
        self._asm_rows = VMRowBase.bootstrap() + self._asm_rows
        return self


def main():
    import argparse
    parser = argparse.ArgumentParser(prog='VM Translater')
    parser.add_argument("src")
    args = parser.parse_args()
    VMTranslater(args.src).write()


if __name__ == '__main__':
    def test():
        def translate(dir1: str, dir2: str):
            p = os.path.abspath(os.path.join(dir1, dir2, dir2 + ".vm"))
            if not os.path.isfile(p):
                p = os.path.abspath(os.path.join(dir1, dir2))
            VMTranslater(p).write()

        stack_arithmetic_dir = os.path.join(__file__, os.pardir, "StackArithmetic")
        translate(stack_arithmetic_dir, "SimpleAdd")
        translate(stack_arithmetic_dir, "StackTest")

        memory_access_dir = os.path.join(__file__, os.pardir, "MemoryAccess")
        translate(memory_access_dir, "BasicTest")
        translate(memory_access_dir, "PointerTest")
        translate(memory_access_dir, "StaticTest")

        function_calls = os.path.join(__file__, os.pardir, os.pardir, "08", "FunctionCalls")
        translate(function_calls, "FibonacciElement")
        translate(function_calls, "NestedCall")
        translate(function_calls, "SimpleFunction")
        translate(function_calls, "StaticsTest")

        program_flow = os.path.join(__file__, os.pardir, os.pardir, "08", "ProgramFlow")
        translate(program_flow, "BasicLoop")
        translate(program_flow, "FibonacciSeries")

    try:
        test()
    except Exception as e:
        logging.debug(str(e))
        main()
