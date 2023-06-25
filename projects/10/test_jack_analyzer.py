import os
from JackAnalyzer import JackAnalyzer


def run_jack_analyzer(folder_name: str):
    input_files = [os.path.join(folder_name, f) for f in os.listdir("ArrayTest") if f.endswith("0.jack")]
    JackAnalyzer(input_files)


def test_array_test():
    run_jack_analyzer("ArrayTest")
