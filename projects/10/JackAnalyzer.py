import os
from argparse import ArgumentParser
from typing import List


class JackAnalyzer:
    def __init__(self, input_files: List[str]):
        for f in input_files:
            assert os.path.isfile(f)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("src", help="jack src file or src dir")
    arg = parser.parse_args()
    print(arg.src)
