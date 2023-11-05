import os
from JackTokenizer import JackTokenizer


class CompilationEngine:
    def __init__(self, tokenizer: JackTokenizer):
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
        self.tk.advance()

    def compile_class(self) -> None:
        """
        Compiles a complete class
        """
        self.tk.advance()
        assert self.tk.token_type() == "keyword"
        assert self.tk.token() == "class"
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

    def compile_class_var_dec(self) -> None:
        """ Compiles a static declaration or a filed declaration. """
        while self.tk.token() in {"static", "field"}:
            self.log("<classVarDec>\n")
            self.indent_level += 1
            self.log_type()

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

            # (
            assert self.tk.token_type() == "symbol"
            self.log_type()

            # parameters of function
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

            assert self.tk.token_type() == "symbol"
            self.log_type()

            # subroutine body
            self.log("<subroutineBody>\n")
            self.indent_level += 1
            assert self.tk.token_type() == "symbol"
            self.log_type()

            self.compile_var_dec()
            self.compile_statements()

            # assert self.tk.token_type == "symbol"
            # self.log_type()
            # self.indent_level -= 1
            # self.log("</subroutineBody>\n")
            # self.indent_level -= 1
            # self.log("</subroutineDec>\n")

    def compile_parameter_list(self) -> None:
        """
        Compiles a (possible empty) parameter list, not including
        the enclosing "{}".
        """
        pass

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