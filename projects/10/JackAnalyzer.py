import os
from argparse import ArgumentParser
from typing import List
from antlr4 import *
from JackLexer import JackLexer
from JackParser import JackParser
from JackListener import JackListener


class JackXMLPrinter(JackListener):
    def __init__(self, xml_path: str):
        self.xml_path = xml_path
        self.fp = None
        self._indent = 0

    def __enter__(self):
        self.fp = open(self.xml_path, "w", newline="")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()

    def enterProg(self, ctx):
        self.fp.write("<class>" + os.linesep)
        self._indent = 1

    def exitProg(self, ctx):
        self.fp.write("</class>" + os.linesep)
        self._indent = 0


class JackAnalyzer:
    def __init__(self, input_files: List[str]):
        self.compile_grammar()
        for f in input_files:
            assert os.path.isfile(f)
            xml_path = f.replace(".jack", ".xml")
            lexer = JackLexer(FileStream(f))
            stream = CommonTokenStream(lexer)
            parser = JackParser(stream)
            tree = parser.prog()

            with JackXMLPrinter(xml_path) as printer:
                walker = ParseTreeWalker()
                walker.walk(printer, tree)

    def compile_grammar(self):
        os.system("antlr4 -Dlanguage=Python3 Jack.g4 ")

if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument("src", help="jack src file or src dir")
    arg = arg_parser.parse_args()
    print(arg.src)
