import os
from JackAnalyzer import JackAnalyzer


def run_jack_analyzer(folder_name: str):
    cwd = os.path.abspath("ArrayTest")
    input_files = [os.path.join(cwd, f) for f in os.listdir("ArrayTest") if f.endswith(".jack")]
    JackAnalyzer(input_files)


def test_jack_analyzer_array_test():
    run_jack_analyzer("ArrayTest")

