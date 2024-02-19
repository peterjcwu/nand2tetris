from glob import glob
import logging
import os
from argparse import ArgumentParser
from typing import List
from tokenizer import Tokenizer
from compilation_engine import CompilationEngine


class JackAnalyzer:
    def __init__(self, file_path: str):
        for f in self.get_files(os.path.abspath(file_path)):
            tokenizer = Tokenizer(f)
            # tokenizer.to_tokens()  # only for debug
            with CompilationEngine(tokenizer) as ce:
                ce.compile_class()

    @staticmethod
    def get_files(file_path: str) -> List[str]:
        # single jack file
        if os.path.isfile(file_path):
            if file_path.endswith(".jack"):
                return [file_path]
            else:
                logging.error("no jack file was found!")
                return []
        # jack file folder
        return list(glob(f"{file_path}/*.jack"))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("src", help="jack src file or src dir")
    arg = parser.parse_args()
    JackAnalyzer(arg.src)
