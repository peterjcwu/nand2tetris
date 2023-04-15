import re
from typing import Dict

from sortedcollections import OrderedSet


def is_num(v: str) -> bool:
    try:
        float(v)
        return True
    except ValueError:
        return False


def padding_left(s: str, length: int, c: str):
    while len(s) < length:
        s = c + s
    return s


class Assembler:
    label_dict: Dict[str, int] = {"R{0}".format(i): i for i in range(16)}

    def __init__(self, asm_path: str) -> None:
        self.label_dict["KBD"] = 24567
        self.label_dict["SCREEN"] = 16384
        self.label_dict["SP"] = 0
        self.label_dict["LCL"] = 1
        self.label_dict["ARG"] = 2
        self.asm_path = asm_path
        self.instructions = []
        self.search_var()
        self.parse()

    def search_var(self):
        label_set = set()
        var_set = OrderedSet()
        with open(self.asm_path) as f_out:
            for line in f_out.readlines():
                if m := re.search(r"\((?P<label>[a-zA-Z0-9\-_]+)\)", line, re.I):
                    label_set.add(m.group("label"))

        with open(self.asm_path) as f_out:
            for line in f_out.readlines():
                line = line.strip()
                if line.startswith("@") and line[1:] not in self.label_dict and line[1:] not in label_set:
                    var_set.add(line[1:])

        for i, var in enumerate(var_set):
            self.label_dict[var] = 15 + i

    def parse(self):
        with open(self.asm_path) as f_in:
            for line in f_in.readlines():
                line = line.split("//")[0].strip()
                if not line:
                    continue
                if m := re.search(r"\((?P<label>[a-zA-Z0-9\-_]+)\)", line, re.I):
                    self.label_dict[m.group("label")] = len(self.instructions)
                elif line.startswith("@"):
                    self.instructions.append(InstructionA(line))

                else:
                    self.instructions.append(InstructionD(line))

    def to_hack(self):
        with open(self.asm_path.replace(".asm", ".hack"), "w") as f_out:
            for i in self.instructions:
                f_out.write(str(i) + "\n")
        return self


class InstructionA:
    def __init__(self, asm_line: str) -> None:
        self.address = asm_line[1:]

    @property
    def address_value(self) -> int:
        if is_num(self.address):
            return int(self.address)
        else:
            return Assembler.label_dict[self.address] 

    def __str__(self) -> str:
        return padding_left("{0:b}".format(int(self.address_value)), 16, "0")


class InstructionD:
    def __init__(self, asm_line: str) -> None:
        self.dst = ""
        self.ctr = ""
        self.jmp = ""
        asm_line = asm_line.strip()
        if ";" in asm_line:
            tokens = asm_line.split(";")
            asm_line, self.jmp = tokens[0], tokens[1].strip()
        if "=" in asm_line:
            tokens = asm_line.split("=")
            self.dst, asm_line = tokens[0].strip(), tokens[1]
        self.ctr = asm_line.strip()
        
    def __str__(self) -> str:
        return "111{0}{1}{2}".format(self.ctr_bit(), self.dst_bit(), self.jmp_bit())

    def ctr_bit(self) -> str:
        if self.ctr == "1":
            return "0" + "111111"
        elif self.ctr == "0":
            return "0" + "101010"
        elif self.ctr == "-1":
            return "0" + "111010"
        elif self.ctr == "D":
            return "0" + "001100"
        elif self.ctr == "!D":
            return "0" + "001101"
        elif self.ctr == "-D":
            return "0" + "001111"
        elif self.ctr == "D+1":
            return "0" + "011111"
        elif self.ctr == "D-1":
            return "0" + "001110"  

        elif self.ctr == "A":
            return "0" + "110000"
        elif self.ctr == "M":
            return "1" + "110000"

        elif self.ctr == "!A":
            return "0" + "110001"
        elif self.ctr == "!M":
            return "1" + "110001"

        elif self.ctr == "-A":
            return "0" + "110011"
        elif self.ctr == "-M":
            return "1" + "110011"

        elif self.ctr == "A+1":
            return "0" + "110111"
        elif self.ctr == "M+1":
            return "1" + "110111"

        elif self.ctr == "A-1":
            return "0" + "110010"
        elif self.ctr == "M-1":
            return "1" + "110010"

        elif self.ctr == "D&A":
            return "0" + "000000"
        elif self.ctr == "D&M":
            return "1" + "000000" 

        elif self.ctr == "D|A":
            return "0" + "010101"
        elif self.ctr == "D|M":
            return "1" + "010101" 

        elif self.ctr == "A-D":
            return "0" + "000111"
        elif self.ctr == "M-D":
            return "1" + "000111" 

        elif self.ctr == "D-A":
            return "0" + "010011"
        elif self.ctr == "D-M":
            return "1" + "010011" 

        elif self.ctr == "D+A":
            return "0" + "000010"
        elif self.ctr == "D+M":
            return "1" + "000010" 

        return "0000000"

    def dst_bit(self) -> str:
        bits = ""
        bits += "1" if "A" in self.dst else "0" 
        bits += "1" if "D" in self.dst else "0"
        bits += "1" if "M" in self.dst else "0"
        return bits

    def jmp_bit(self) -> str:
        if self.jmp == "":
            return "000"
        elif self.jmp.upper() == "JGT":
            return "001"
        elif self.jmp.upper() == "JEQ":
            return "010"
        elif self.jmp.upper() == "JGE":
            return "011"
        elif self.jmp.upper() == "JLT":
            return "100"
        elif self.jmp.upper() == "JNE":
            return "101"
        elif self.jmp.upper() == "JLE":
            return "110"
        elif self.jmp.upper() == "JMP":
            return "111" 


if __name__ == "__main__":
    import os
    # Assembler(os.path.join(__file__, os.pardir, "add", "Add.asm")).to_hack()
    # Assembler(os.path.join(__file__, os.pardir, "max", "Max.asm")).to_hack()
    # Assembler(os.path.join(__file__, os.pardir, "rect", "Rect.asm")).to_hack()
    a = Assembler(os.path.join(__file__, os.pardir, "Pong", "PongL.asm")).to_hack()
    print()
