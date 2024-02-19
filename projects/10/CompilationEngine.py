import logging
import os
from tokenizer import Tokenizer


class CompilationEngine:
    def __init__(self, tokenizer: Tokenizer):
        self.tk = tokenizer
        self.xml_path = os.path.splitext(tokenizer.file_path)[0] + ".xml"
        self.indent_level = 0
        self.fp = None

    def __enter__(self):
        self.fp = open(self.xml_path, "w", newline="")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()

    def log(self, tag: str):
        self.fp.write("  " * self.indent_level + tag)

    def log_type(self):
        token_type = self.tk.token_type()
        token = self.tk.token()
        self.fp.write("  " * self.indent_level + f"<{token_type}> {token} </{token_type}>\n")
        try:
            self.tk.advance()
        except Exception as e:
            logging.debug(str(e))

    def compile_class(self) -> None:
        """ Compiles a complete class """
        self.tk.advance()
        assert self.tk.token_type() == "keyword"
        assert self.tk.token() == "class", f"'{self.tk.token()}' != 'class'..."
        self.log("<class>\n")
        self.indent_level += 1
        self.log_type()

        # identifier
        assert self.tk.token_type() == "identifier"
        self.log_type()

        # {
        assert self.tk.token_type() == "symbol"
        self.log_type()

        self.compile_class_var_dec()
        self.compile_subroutine()

        self.log_type()
        self.indent_level -= 1
        self.log("</class>\n")

    def compile_class_var_dec(self) -> None:
        """ Compiles a static declaration or a filed declaration. """
        while self.tk.token() in {"static", "field"}:
            self.log("<classVarDec>\n")
            self.indent_level += 1
            self.log_type()

            assert self.tk.token() in {"boolean", "int", "char"} or self.tk.is_identifier()
            self.log_type()

            assert self.tk.is_identifier()
            self.log_type()

            while self.tk.is_symbol():
                symbol = self.tk.token()
                if symbol == ";":
                    self.log_type()
                    break
                elif symbol == ",":
                    self.log_type()
                    assert self.tk.is_identifier()
                    self.log_type()

            self.indent_level -= 1
            self.log("</classVarDec>\n")

    def compile_subroutine(self) -> None:
        """ Compiles a complete method, function or constructor. """
        while self.tk.token() in {"function", "method", "constructor"}:
            self.log("<subroutineDec>\n")
            self.indent_level += 1
            self.log_type()

            assert self.tk.token_type() in {"identifier", "keyword"}
            self.log_type()

            # function name
            assert self.tk.token_type() == "identifier"
            self.log_type()
            self.compile_parameter_list()

            # subroutine body
            self.log("<subroutineBody>\n")
            self.indent_level += 1
            assert self.tk.token_type() == "symbol"
            self.log_type()

            self.compile_var_dec()
            self.compile_statements()

            assert self.tk.is_symbol()
            self.log_type()

            self.indent_level -= 1
            self.log("</subroutineBody>\n")
            self.indent_level -= 1
            self.log("</subroutineDec>\n")

    def compile_parameter_list(self) -> None:
        """ Compiles a (possible empty) parameter list, not including the enclosing "{}" """
        # (
        assert self.tk.token_type() == "symbol"
        self.log_type()

        self.log("<parameterList>\n")
        self.indent_level += 1
        while self.tk.token_type() in {"identifier", "keyword"}:
            self.log_type()

            assert self.tk.token_type() == "identifier"
            self.log_type()

            assert self.tk.token_type() == "symbol"
            if self.tk.token() == ")":
                break
            self.log_type()

        self.indent_level -= 1
        self.log("</parameterList>\n")

        # )
        assert self.tk.token_type() == "symbol"
        self.log_type()

    def compile_var_dec(self) -> None:
        """ Compiles a var declaration """
        while self.tk.token() == "var":
            self.log("<varDec>\n")
            self.indent_level += 1
            self.log_type()

            assert self.tk.token() in {"char", "boolean", "int"} or self.tk.token_type() == "identifier"
            self.log_type()

            assert self.tk.token_type() == "identifier"
            self.log_type()

            while self.tk.token_type() == "symbol":
                if self.tk.token() == ";":
                    self.log_type()
                    break
                elif self.tk.token() == ",":
                    self.log_type()
                    assert self.tk.token_type() == "identifier"
                    self.log_type()

            self.indent_level -= 1
            self.log("</varDec>\n")

    def compile_statements(self) -> None:
        """ Compiles a sequence of statements, not including the enclosing '{}' """
        self.log("<statements>\n")
        self.indent_level += 1
        while self.tk.token() in {"return", "do", "let", "if", "while"}:
            if self.tk.token() == "return":
                self.compile_return()
            elif self.tk.token() == "do":
                self.compile_do()
            elif self.tk.token() == "let":
                self.compile_let()
            elif self.tk.token() == "if":
                self.compile_if()
            elif self.tk.token() == "while":
                self.compile_while()
        self.indent_level -= 1
        self.log("</statements>\n")

    def compile_return(self) -> None:
        self.log("<returnStatement>\n")
        self.indent_level += 1
        self.log_type()
        if self.tk.is_symbol():
            self.log_type()
        elif self.tk.is_identifier() or self.tk.is_keyword():
            self.compile_expression()
            assert self.tk.is_symbol()
            self.log_type()
        else:
            raise Exception("Error")
        self.indent_level -= 1
        self.log("</returnStatement>\n")

    def compile_do(self) -> None:
        self.log("<doStatement>\n")
        self.indent_level += 1
        self.log_type()
        assert self.tk.is_identifier()
        self.log_type()
        if self.tk.token() == "[":
            self.log_type()
            self.compile_expression()
            assert self.tk.is_symbol() and self.tk.token() == "]"
            self.log_type()

        assert self.tk.is_symbol()
        symbol = self.tk.token()
        self.log_type()
        if symbol == ".":
            assert self.tk.is_identifier()
            self.log_type()
            assert self.tk.is_symbol()
            self.log_type()
        elif symbol != "(":
            raise Exception("Error")

        self.compile_expression_list()

        assert self.tk.is_symbol()
        self.log_type()

        assert self.tk.is_symbol()
        self.log_type()

        self.indent_level -= 1
        self.log("</doStatement>\n")

    def compile_let(self) -> None:
        self.log("<letStatement>\n")
        self.indent_level += 1
        self.log_type()

        assert self.tk.is_identifier()
        self.log_type()

        if self.tk.token() == "[":
            self.log_type()
            self.compile_expression()
            assert self.tk.is_symbol() and self.tk.token() == "]"
            self.log_type()

        assert self.tk.is_symbol()
        self.log_type()

        self.compile_expression()
        assert self.tk.is_symbol()
        self.log_type()

        self.indent_level -= 1
        self.log("</letStatement>\n")

    def compile_while(self) -> None:
        self.log("<whileStatement>\n")
        self.indent_level += 1
        self.log_type()

        assert self.tk.is_symbol()
        self.log_type()

        self.compile_expression()

        assert self.tk.is_symbol()
        self.log_type()

        assert self.tk.is_symbol()
        self.log_type()

        self.compile_statements()

        assert self.tk.is_symbol()
        self.log_type()

        self.indent_level -= 1
        self.log("</whileStatement>\n")

    def compile_if(self) -> None:
        self.log("<ifStatement>\n")
        self.indent_level += 1
        self.log_type()

        assert self.tk.is_symbol()
        self.log_type()

        self.compile_expression()

        assert self.tk.is_symbol()
        self.log_type()

        assert self.tk.is_symbol()
        self.log_type()

        self.compile_statements()

        assert self.tk.is_symbol()
        self.log_type()

        if self.tk.token() == "else":
            self.compile_else_statement()

        self.indent_level -= 1
        self.log("</ifStatement>\n")

    def compile_else_statement(self) -> None:
        self.log_type()
        assert self.tk.is_symbol() and self.tk.token() == "{"
        self.log_type()

        self.compile_statements()

        assert self.tk.is_symbol() and self.tk.token() == "}"
        self.log_type()

    def compile_expression(self) -> None:
        self.log("<expression>\n")
        self.indent_level += 1
        self.compile_term()
        while self.tk.token() in {"+", "-", "*", "/", "&amp;", "|", "&lt;", "&gt;", "="}:
            self.log_type()
            self.compile_term()
        self.indent_level -= 1
        self.log("</expression>\n")

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
        self.log("<term>\n")
        self.indent_level += 1
        if self.tk.is_identifier() or self.tk.is_keyword():
            self.log_type()
            if self.tk.is_symbol():
                symbol = self.tk.token()
                if symbol == ".":
                    self.log_type()
                    assert self.tk.is_identifier()
                    self.log_type()

                    assert self.tk.is_symbol()
                    self.log_type()

                    self.compile_expression_list()

                    assert self.tk.is_symbol()
                    self.log_type()

                elif symbol == "[":
                    self.log_type()
                    self.compile_expression()
                    assert self.tk.token() == "]"
                    self.log_type()
        elif self.tk.is_string_contant() or self.tk.is_integer_constant():
            self.log_type()

        elif self.tk.is_symbol():
            symbol = self.tk.token()
            if symbol == "(":
                self.log_type()
                self.compile_expression()
                assert self.tk.token() == ")"
                self.log_type()
            elif symbol in {"-", "~"}:
                self.log_type()
                self.compile_term()
            else:
                raise Exception("Error")

        self.indent_level -= 1
        self.log("</term>\n")

    def compile_expression_list(self) -> None:
        """ Compiles a (possibly empty) comma-separated list of expressions """
        self.log("<expressionList>\n")
        self.indent_level += 1
        while not self.tk.is_symbol() or self.tk.token() == "(":
            self.compile_expression()
            assert self.tk.is_symbol()
            if self.tk.token() == ")":
                break
            self.log_type()
        self.indent_level -= 1
        self.log("</expressionList>\n")
