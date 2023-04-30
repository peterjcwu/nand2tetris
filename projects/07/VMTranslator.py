import os
import re
from abc import ABC
from typing import List
_label_counter = 0


class VMRowBase(ABC):
    MATCH_RE = re.compile(r".*")

    def __init__(self):
        self.line: str = ""
        self.lno: int = 0

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
            '@13',
            'M=D',
            '@SP',
            'AM=M-1',
            'D=M',
            '@13',
            'D=D-M',
        ]

    @staticmethod
    def comparison(jump_type: str, pass_label: str, after_label: str):
        return [
            f'@{pass_label}',
            jump_type,
            '@SP',
            'A=M',
            'M=0',
            '@SP',
            'M=M+1',
            f'@{after_label}',
            '0;JMP',
            f'({pass_label})',
            '@SP',
            'A=M',
            'M=-1',
            '@SP',
            'M=M+1',
            f'({after_label})',
        ]


class VMRowSub(VMRowBase):
    MATCH_RE = re.compile(r"sub", re.I)

    def to_asm(self) -> List[str]:
        return [
            '// -- sub --',
            '@SP',
            'AM=M-1',
            'D=M',
            '@SP',
            'AM=M-1',
            'D=M-D',
            'M=D',
            '@SP',
            'M=M+1',
            '',
        ]


class VMRowNeg(VMRowBase):
    MATCH_RE = re.compile(r"neq", re.I)

    def to_asm(self) -> List[str]:
        return [
            '//--negate--',
            '@SP',
            'AM=M-1',
            'M=-M',
            '@SP',
            'M=M+1',
        ]


class VMRowAdd(VMRowBase):
    MATCH_RE = re.compile(r"^add", re.I)

    def to_asm(self) -> List[str]:
        return [
            f"// -- {self.line} --",
            '@SP',
            'AM=M-1',
            'D=M',
            '@SP',
            'AM=M-1',
            'D=D+M',
            'M=D',
            '@SP',
            'M=M+1',
            ""
        ]


class VMRowInit(VMRowBase):
    def to_asm(self) -> List[str]:
        return [
            "// -- init --",
            "@256",
            "D=A",
            "@SP",
            "M=D",
        ]


class VMRowEq(VMRowBase):
    MATCH_RE = re.compile(r"^eq", re.I)

    def to_asm(self) -> List[str]:
        return [
            '// -- eq -- ',
            *self.comparison_pre,
            *self.comparison('D;JEQ', self.get_label("eq.pass"), self.get_label("eq.after")),
            "",
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
            '@SP',
            'AM=M-1',
            'D=D&M',
            'M=D',
            '@SP',
            'M=M+1',
        ]


class VMRowOr(VMRowBase):
    MATCH_RE = re.compile(r"^or", re.I)

    def to_asm(self) -> List[str]:
        return [
            '// -- or --',
            '@SP',
            'AM=M-1',
            'D=M',
            '@SP',
            'AM=M-1',
            'D=D|M',
            'M=D',
            '@SP',
            'M=M+1'
        ]


class VMRowNot(VMRowBase):
    MATCH_RE = re.compile(r"^not", re.I)

    def to_asm(self) -> List[str]:
        return [
            '// -- not --',
            '@SP',
            'AM=M-1',
            'M=!M',
            '@SP',
            'M=M+1',
        ]


class VMRowPush(VMRowBase):
    MATCH_RE = re.compile("^push", re.I)

    def __init__(self):
        VMRowBase.__init__(self)
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

        elif self.var_type == "static":  # r16-r254
            assert self.val <= 238, f"Static value cannot exceed 238 at line {self.lno}"
            return self.to_asm_offset_push(16)

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
            rows = self.to_asm_offset_pop(3)
        elif self.var_type == "temp":
            assert self.val <= 7
            rows = self.to_asm_offset_pop(5)
        elif self.var_type == "static":
            assert self.val <= 238
            rows = self.to_asm_offset_pop(16)
        else:
            rows = self.to_asm_name_pop()
        return [f"// -- {self.line} -- "] + rows + self._footer

    @property
    def _footer(self) -> List[str]:
        return [
            "@SP",
            "AM=M-1",
            "D=M",
            "@14",
            "A=M",
            "M=D",
        ]

    def to_asm_offset_pop(self, base_val: int) -> List[str]:
        return [
            f"@{self.val + base_val}",
            "D=A",
            "@14",
            "M=D",
        ]

    def to_asm_name_pop(self) -> List[str]:
        return [
            f"@{self.val}",
            "D=A",
            f"@{self.RESERVED_LOC[self.var_type]}",
            "D=D+M",
            "@14",
            "M=D",
        ]


class VMTranslater:
    def __init__(self, src: str):
        # read
        self.src = os.path.abspath(src)
        self._asm_rows: List[str] = [r for r in VMRowInit().to_asm()]
        self._vm_row_types: List[VMRowBase] = [
            VMRowSub(),
            VMRowNeg(),
            VMRowAdd(),
            VMRowEq(),
            VMRowGt(),
            VMRowLt(),
            VMRowAnd(),
            VMRowOr(),
            VMRowNot(),
            VMRowPop(),
            VMRowPush(),
        ]
        # read
        self._read(self.src)
        # write
        self.dst = re.sub(r"\.vm$", ".asm", self.src)
        self._write(self.dst)

    def _read(self, src: str):
        with open(src, "r") as f_in:
            for i, line in enumerate(f_in.readlines()):
                line = re.sub("//.*", "", line).strip()
                if not line:
                    continue
                for vm_row_type in self._vm_row_types:
                    vm_row_type.update(line, i + 1)
                    if vm_row_type.match():
                        self._asm_rows.extend(vm_row_type.to_asm())

    def _write(self, dst: str):
        with open(dst, "w", newline="") as f_out:
            for asm_row in self._asm_rows:
                f_out.write(asm_row + os.linesep)


def main():
    import argparse
    parser = argparse.ArgumentParser(prog='VM Translater')
    parser.add_argument("src")
    args = parser.parse_args()
    VMTranslater(args.src)


if __name__ == '__main__':
    def test():
        def translate(dir1: str, dir2: str):
            p = os.path.abspath(os.path.join(dir1, dir2, dir2 + ".vm"))
            VMTranslater(p)

        stack_arithmetic_dir = os.path.join(__file__, os.pardir, "StackArithmetic")
        translate(stack_arithmetic_dir, "SimpleAdd")
        translate(stack_arithmetic_dir, "StackTest")

        memory_access_dir = os.path.join(__file__, os.pardir, "MemoryAccess")
        translate(memory_access_dir, "BasicTest")
        translate(memory_access_dir, "PointerTest")
        translate(memory_access_dir, "StaticTest")

    # test()
    main()
