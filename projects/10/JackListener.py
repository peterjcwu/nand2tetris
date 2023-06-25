# Generated from Jack.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .JackParser import JackParser
else:
    from JackParser import JackParser

# This class defines a complete listener for a parse tree produced by JackParser.
class JackListener(ParseTreeListener):

    # Enter a parse tree produced by JackParser#prog.
    def enterProg(self, ctx:JackParser.ProgContext):
        pass

    # Exit a parse tree produced by JackParser#prog.
    def exitProg(self, ctx:JackParser.ProgContext):
        pass


    # Enter a parse tree produced by JackParser#subroutineDec.
    def enterSubroutineDec(self, ctx:JackParser.SubroutineDecContext):
        pass

    # Exit a parse tree produced by JackParser#subroutineDec.
    def exitSubroutineDec(self, ctx:JackParser.SubroutineDecContext):
        pass


    # Enter a parse tree produced by JackParser#parameterList.
    def enterParameterList(self, ctx:JackParser.ParameterListContext):
        pass

    # Exit a parse tree produced by JackParser#parameterList.
    def exitParameterList(self, ctx:JackParser.ParameterListContext):
        pass


    # Enter a parse tree produced by JackParser#subroutineBody.
    def enterSubroutineBody(self, ctx:JackParser.SubroutineBodyContext):
        pass

    # Exit a parse tree produced by JackParser#subroutineBody.
    def exitSubroutineBody(self, ctx:JackParser.SubroutineBodyContext):
        pass


    # Enter a parse tree produced by JackParser#varDec.
    def enterVarDec(self, ctx:JackParser.VarDecContext):
        pass

    # Exit a parse tree produced by JackParser#varDec.
    def exitVarDec(self, ctx:JackParser.VarDecContext):
        pass


    # Enter a parse tree produced by JackParser#statement.
    def enterStatement(self, ctx:JackParser.StatementContext):
        pass

    # Exit a parse tree produced by JackParser#statement.
    def exitStatement(self, ctx:JackParser.StatementContext):
        pass


    # Enter a parse tree produced by JackParser#letStatement.
    def enterLetStatement(self, ctx:JackParser.LetStatementContext):
        pass

    # Exit a parse tree produced by JackParser#letStatement.
    def exitLetStatement(self, ctx:JackParser.LetStatementContext):
        pass


    # Enter a parse tree produced by JackParser#expression.
    def enterExpression(self, ctx:JackParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JackParser#expression.
    def exitExpression(self, ctx:JackParser.ExpressionContext):
        pass


    # Enter a parse tree produced by JackParser#term.
    def enterTerm(self, ctx:JackParser.TermContext):
        pass

    # Exit a parse tree produced by JackParser#term.
    def exitTerm(self, ctx:JackParser.TermContext):
        pass


    # Enter a parse tree produced by JackParser#stringConstant.
    def enterStringConstant(self, ctx:JackParser.StringConstantContext):
        pass

    # Exit a parse tree produced by JackParser#stringConstant.
    def exitStringConstant(self, ctx:JackParser.StringConstantContext):
        pass


    # Enter a parse tree produced by JackParser#whileStatement.
    def enterWhileStatement(self, ctx:JackParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by JackParser#whileStatement.
    def exitWhileStatement(self, ctx:JackParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by JackParser#type.
    def enterType(self, ctx:JackParser.TypeContext):
        pass

    # Exit a parse tree produced by JackParser#type.
    def exitType(self, ctx:JackParser.TypeContext):
        pass



del JackParser