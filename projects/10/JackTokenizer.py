import itertools
import os
import re
from typing import Set, List


class JackTokenizer:
    TOKEN_TYPES = {"keyword", "symbol", "identifier", "integerConstant", "stringConstant"}
    KEY_WORDS = {"class", "method", "function", "constructor", "int", "boolean", "char", "void", "var",
                 "static", "field", "let", "do", "if", "else", "while", "return", "true", "false", "null", "this"}
    SYMBOLS: Set[str] = {'{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|',
                         '<', '>', '=', '~'}

    def __init__(self, file_path: str):
        self.file_path = file_path

        with open(self.file_path) as f_in:
            lines: List[str] = []
            for line in f_in.readlines():
                line = line.split("//")[0]
                line = line.strip()
                if line:
                    lines.append(line)

        text = " ".join(lines)
        text = re.sub(r"/\*.*?\*/", "", text)

        # replace string literals with number
        self.string_literals = re.findall(r'\".*?\"', text)
        for i, s in enumerate(self.string_literals):
            text = text.replace(s, f"\\{i}\\")

        self.stack = list(itertools.chain(*[[a for a in self._advance(t)] for t in re.split(r"\s+", text)]))
        self.i = -1

    def has_more_tokens(self) -> bool:
        return self.i + 1 < len(self.stack)

    def advance(self) -> str:
        """
        Gets the next token from the input and makes it the current token
        This method should be called if the has_more_tokens is True.
        """
        self.i += 1
        token_types, token = self.stack[self.i]
        return token

    def token_type(self) -> str:
        return self.stack[self.i][0]

    def token(self) -> str:
        return self.stack[self.i][1]

    def _advance(self, t: str):
        cur_token = ""
        i = 0
        while i < len(t):
            cur_token += t[i]
            # keyword
            if cur_token in self.KEY_WORDS:
                yield "keyword", cur_token
                cur_token = ""
                i += 1

            # string const
            elif cur_token == "\\":
                while i + 1 < len(t) and t[i + 1] != "\\":
                    cur_token += t[i + 1]
                    i += 1
                cur_token = cur_token.replace("\\", "")
                yield "stringConstant", self.string_literals[int(cur_token)].replace('"', "")
                cur_token = ""
                i += 2  # last \\

            # symbols
            elif t[i] in self.SYMBOLS:
                if len(cur_token) > 1:
                    yield "identifier", cur_token[:-1]
                if t[i] == ">":
                    yield "symbol",  "&gt;"
                elif t[i] == "<":
                    yield "symbol", "&lt;"

                elif t[i] == "&":
                    yield "symbol", "&amp;"
                else:
                    yield "symbol", t[i]
                cur_token = ""
                i += 1

            # integer const
            elif self.is_num(cur_token):
                while i + 1 < len(t) and self.is_num(cur_token + t[i+1]):
                    cur_token = cur_token + t[i+1]
                    i += 1
                yield "integerConstant", cur_token
                cur_token = ""
                i += 1
            else:
                i += 1
        if cur_token:
            yield "identifier", cur_token

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

    def to_tokens(self):
        dst = os.path.splitext(self.file_path)[0] + "T.xml"
        with open(dst, "w", newline="") as f_out:
            f_out.write("<tokens>" + os.linesep)
            while self.has_more_tokens():
                token = self.advance()
                f_out.write(f"<{self.token_type()}> {token} </{self.token_type()}>" + os.linesep)
            f_out.write("</tokens>" + os.linesep)
        # reset
        self.i = -1

    def is_keyword(self) -> bool:
        return self.token_type() == "keyword"

    def is_symbol(self) -> bool:
        return self.token_type() == "symbol"

    def is_identifier(self) -> bool:
        return self.token_type() == "identifier"

    def is_integer_constant(self) -> bool:
        return self.token_type() == "integerConstant"

    def is_string_contant(self) -> bool:
        return self.token_type() == "stringConstant"
