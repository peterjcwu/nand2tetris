import os
import sys
sys.path.append(os.path.join(__file__, os.pardir))
from glob import glob
from compilation_engine import CompilationEngine


class JackCompiler:
    def __init__(self, src: str):
        self.src: str = src
        for in_file in self._get_files():
            out_file = in_file.replace(".jack", ".vm")
            CompilationEngine(in_file, out_file)

    def _get_files(self):
        # single jack file
        if os.path.isfile(self.src):
            if self.src.endswith(".jack"):
                return [self.src]
            else:
                raise Exception("no jack file was found!")
        # jack file folder
        return glob(f"{self.src}/*.jack")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: python3 JackCompiler.py <.jack>")
    else:
        JackCompiler(sys.argv[1])
