import os
import re
from argparse import ArgumentParser
from typing import List, Set, Tuple


class JackTokenizer:
    TOKEN_TYPES = {"keyword", "symbol", "identifier", "integerConstant", "stringConstant"}
    KEY_WORDS = {"class", "method", "function", "constructor", "int", "boolean", "char", "void", "var",
                 "static", "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this"}
    SYMBOLS: Set[str] = {'{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|',
                         '<', '>', '=', '~'}

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.tokens: List[Tuple[str, str]] = []

        with open(self.file_path) as f_in:
            lines: List[str] = []
            for line in f_in.readlines():
                line = line.split("//")[0]
                line = line.strip()
                if line:
                    lines.append(line)
        self.advance(" ".join(lines))

    def to_tokens(self):
        dst = os.path.splitext(self.file_path)[0] + "T.xml"
        with open(dst, "w", newline="") as f_out:
            f_out.write("<tokens>" + os.linesep)
            for k, v in self.tokens:
                f_out.write(f"<{k}> {v} </{k}>"+ os.linesep)
            f_out.write("</tokens>" + os.linesep)

    def advance(self, text: str) -> None:
        """
        Gets the next token from the input and makes it the current token
        This method should be called if the has_more_tokens is True.
        :return: None
        """
        text = re.sub(r"/\*.*\*/", "", text)
        string_literals = re.findall(r'\".*?\"', text)
        for i, s in enumerate(string_literals):
            text = text.replace(s, f"\\{i}\\")

        for t in re.split(r"\s+", text):
            cur_token = ""
            i = 0
            while i < len(t):
                cur_token += t[i]
                # keyword
                if cur_token in self.KEY_WORDS:
                    self.tokens.append(("keyword", cur_token))
                    cur_token = ""
                    i += 1

                # string const
                elif cur_token == "\\":
                    while i + 1 < len(t) and t[i + 1] != "\\":
                        cur_token += t[i + 1]
                        i += 1
                    cur_token = cur_token.replace("\\", "")
                    self.tokens.append(("stringConstant", string_literals[int(cur_token)].replace('"', "")))
                    cur_token = ""
                    i += 2  # last \\

                # symbols
                elif t[i] in self.SYMBOLS:
                    if len(cur_token) > 1:
                        self.tokens.append(("identifier", cur_token[:-1]))
                    if t[i] == ">":
                        self.tokens.append(("symbol",  "&gt;"))
                    elif t[i] == "<":
                        self.tokens.append(("symbol", "&lt;"))
                    else:
                        self.tokens.append(("symbol", t[i]))
                    cur_token = ""
                    i += 1

                # integer const
                elif self.is_num(cur_token):
                    while i + 1 < len(t) and self.is_num(cur_token + t[i+1]):
                        cur_token = cur_token + t[i+1]
                        i += 1
                    self.tokens.append(("integerConstant", cur_token))
                    cur_token = ""
                    i += 1
                else:
                    i += 1
            if cur_token:
                self.tokens.append(("identifier", cur_token))

    @staticmethod
    def is_num(val: any) -> bool:
        try:
            float(val)
            return True
        except ValueError:
            return False

    @property
    def symbol(self) -> str:
        """
        Should be called only when token_type is SYMBOL
        :return: the character which is the current token
        """
        return ""

    @property
    def identifier(self) -> str:
        """
        Should be called only when token_type is IDENTIFIER
        :return: the identifier which is the current token
        """
        return ""

    @property
    def int_val(self) -> int:
        """
        Should be called only when token_type is INT_CONST
        :return: the integer value of the current token
        """
        return 0

    @property
    def string_val(self) -> str:
        """
        Should be called only when token_type is STRING_CONST
        :return: the string value of the current token
        """
        return ""


class CompilationEngine:
    def __init__(self, tokenizer: JackTokenizer):
        self.tokenizer = tokenizer
        self.xml_path = os.path.splitext(tokenizer.file_path)[0] + ".xml"
        self.indent = 0
        self.fp = None

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def to_xml(self):
        with open(self.xml_path, "w", newline="") as f_out:
            self.compile_class()

    def compile_class(self) -> None:
        """
        Compiles a complete class
        """
        v, t = self.tokenizer.tokens.pop(0)
        print()

    def compile_class_var_dec(self) -> None:
        """
        Compiles a static declaration or a filed declaration.
        """
        pass

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function or constructor.
        """
        pass

    def compile_parameter_list(self) -> None:
        """
        Compiles a (possible empty) parameter list, not including
        the enclosing "{}".
        """
        pass

    def compile_var_dec(self) -> None:
        """
        Compiles a var declaration
        """
        pass

    def compile_statements(self) -> None:
        """
        Compiles a sequence of statements, not including the
        enclosing "{}".
        """
        pass

    def compile_do(self) -> None:
        pass

    def compile_let(self) -> None:
        pass

    def compile_while(self) -> None:
        pass

    def compile_return(self) -> None:
        pass

    def compile_if(self) -> None:
        pass

    def compile_expression(self) -> None:
        pass

    def compile_term(self) -> None:
        """
        Compiles a term. This routine is faced with a slight difficulty  when
        trying to decide between some alternative parsing rules.
        Specifically, if the current token is an identifier, the routine
        must distinguish between a variable, an array entry, and a subroutine
        call. A single look-ahead token, which may be one of "|", "(", or "."
        suffices to distinguish between the three possibilities. Any other token
        is not part of the term and should not be advance over.
        """
        pass

    def compile_expression_list(self) -> None:
        """
        Compiles a (possibly empty) comma-separated list of expressions.
        """


class JackAnalyzer:
    def __init__(self, input_files: List[str]):
        for f in input_files:
            assert os.path.isfile(f)


if __name__ == '__main__':
    from glob import glob
    import logging

    def main(file_path: str):
        for f in get_files(os.path.abspath(file_path)):
            tokenizer = JackTokenizer(f)
            tokenizer.to_tokens()  # only for debug
            compilation_engine = CompilationEngine(tokenizer)
            compilation_engine.to_xml()

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


    parser = ArgumentParser()
    parser.add_argument("src", help="jack src file or src dir")
    arg = parser.parse_args()
    main(arg.src)
