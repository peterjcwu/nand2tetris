# Generated from Jack.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,3,
        2,45,8,2,1,3,1,3,4,3,49,8,3,11,3,12,3,50,1,4,1,4,1,4,1,4,1,4,1,5,
        1,5,3,5,60,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,
        9,3,9,75,8,9,1,10,1,10,1,10,1,10,1,10,1,10,4,10,83,8,10,11,10,12,
        10,84,1,10,1,10,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,
        22,0,1,1,0,8,11,84,0,24,1,0,0,0,2,30,1,0,0,0,4,44,1,0,0,0,6,48,1,
        0,0,0,8,52,1,0,0,0,10,59,1,0,0,0,12,61,1,0,0,0,14,67,1,0,0,0,16,
        69,1,0,0,0,18,74,1,0,0,0,20,76,1,0,0,0,22,88,1,0,0,0,24,25,5,1,0,
        0,25,26,5,23,0,0,26,27,5,33,0,0,27,28,3,2,1,0,28,29,5,33,0,0,29,
        1,1,0,0,0,30,31,5,3,0,0,31,32,3,22,11,0,32,33,5,23,0,0,33,34,5,24,
        0,0,34,35,3,4,2,0,35,36,5,25,0,0,36,37,5,26,0,0,37,38,3,6,3,0,38,
        39,5,21,0,0,39,40,5,30,0,0,40,41,5,27,0,0,41,3,1,0,0,0,42,45,5,34,
        0,0,43,45,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,5,1,0,0,0,46,49,
        3,8,4,0,47,49,3,10,5,0,48,46,1,0,0,0,48,47,1,0,0,0,49,50,1,0,0,0,
        50,48,1,0,0,0,50,51,1,0,0,0,51,7,1,0,0,0,52,53,5,7,0,0,53,54,5,23,
        0,0,54,55,5,23,0,0,55,56,5,30,0,0,56,9,1,0,0,0,57,60,3,12,6,0,58,
        60,3,20,10,0,59,57,1,0,0,0,59,58,1,0,0,0,60,11,1,0,0,0,61,62,5,16,
        0,0,62,63,5,23,0,0,63,64,5,37,0,0,64,65,3,14,7,0,65,66,5,30,0,0,
        66,13,1,0,0,0,67,68,3,16,8,0,68,15,1,0,0,0,69,70,3,18,9,0,70,17,
        1,0,0,0,71,72,5,23,0,0,72,75,3,18,9,0,73,75,5,23,0,0,74,71,1,0,0,
        0,74,73,1,0,0,0,75,19,1,0,0,0,76,77,5,20,0,0,77,78,5,24,0,0,78,79,
        3,14,7,0,79,80,5,25,0,0,80,82,5,26,0,0,81,83,3,10,5,0,82,81,1,0,
        0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,
        5,27,0,0,87,21,1,0,0,0,88,89,7,0,0,0,89,23,1,0,0,0,6,44,48,50,59,
        74,84
    ]

class JackParser ( Parser ):

    grammarFileName = "Jack.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'constructor'", "'function'", 
                     "'method'", "'field'", "'static'", "'var'", "'int'", 
                     "'char'", "'boolean'", "'void'", "'true'", "'false'", 
                     "'null'", "'this'", "'let'", "'do'", "'if'", "'else'", 
                     "'while'", "'return'", "<INVALID>", "<INVALID>", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "CONSTRUCTOR", "FUNCTION", "METHOD", 
                      "FIELD", "STATIC", "VAR", "INT", "CHAR", "BOOLEAN", 
                      "VOID", "TRUE", "FALSE", "NULL", "THIS", "LET", "DO", 
                      "IF", "ELSE", "WHILE", "RETURN", "KEYWORD", "Identifier", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "SEMI", "COMMA", "DOT", "SYMBOL", "WS", 
                      "COMMENT", "LINE_COMMENT", "EQUAL" ]

    RULE_prog = 0
    RULE_subroutineDec = 1
    RULE_parameterList = 2
    RULE_subroutineBody = 3
    RULE_varDec = 4
    RULE_statement = 5
    RULE_letStatement = 6
    RULE_expression = 7
    RULE_term = 8
    RULE_stringConstant = 9
    RULE_whileStatement = 10
    RULE_type = 11

    ruleNames =  [ "prog", "subroutineDec", "parameterList", "subroutineBody", 
                   "varDec", "statement", "letStatement", "expression", 
                   "term", "stringConstant", "whileStatement", "type" ]

    EOF = Token.EOF
    CLASS=1
    CONSTRUCTOR=2
    FUNCTION=3
    METHOD=4
    FIELD=5
    STATIC=6
    VAR=7
    INT=8
    CHAR=9
    BOOLEAN=10
    VOID=11
    TRUE=12
    FALSE=13
    NULL=14
    THIS=15
    LET=16
    DO=17
    IF=18
    ELSE=19
    WHILE=20
    RETURN=21
    KEYWORD=22
    Identifier=23
    LPAREN=24
    RPAREN=25
    LBRACE=26
    RBRACE=27
    LBRACK=28
    RBRACK=29
    SEMI=30
    COMMA=31
    DOT=32
    SYMBOL=33
    WS=34
    COMMENT=35
    LINE_COMMENT=36
    EQUAL=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(JackParser.CLASS, 0)

        def Identifier(self):
            return self.getToken(JackParser.Identifier, 0)

        def SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(JackParser.SYMBOL)
            else:
                return self.getToken(JackParser.SYMBOL, i)

        def subroutineDec(self):
            return self.getTypedRuleContext(JackParser.SubroutineDecContext,0)


        def getRuleIndex(self):
            return JackParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = JackParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(JackParser.CLASS)
            self.state = 25
            self.match(JackParser.Identifier)
            self.state = 26
            self.match(JackParser.SYMBOL)
            self.state = 27
            self.subroutineDec()
            self.state = 28
            self.match(JackParser.SYMBOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubroutineDecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(JackParser.FUNCTION, 0)

        def type_(self):
            return self.getTypedRuleContext(JackParser.TypeContext,0)


        def Identifier(self):
            return self.getToken(JackParser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(JackParser.LPAREN, 0)

        def parameterList(self):
            return self.getTypedRuleContext(JackParser.ParameterListContext,0)


        def RPAREN(self):
            return self.getToken(JackParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(JackParser.LBRACE, 0)

        def subroutineBody(self):
            return self.getTypedRuleContext(JackParser.SubroutineBodyContext,0)


        def RETURN(self):
            return self.getToken(JackParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(JackParser.SEMI, 0)

        def RBRACE(self):
            return self.getToken(JackParser.RBRACE, 0)

        def getRuleIndex(self):
            return JackParser.RULE_subroutineDec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubroutineDec" ):
                listener.enterSubroutineDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubroutineDec" ):
                listener.exitSubroutineDec(self)




    def subroutineDec(self):

        localctx = JackParser.SubroutineDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_subroutineDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(JackParser.FUNCTION)
            self.state = 31
            self.type_()
            self.state = 32
            self.match(JackParser.Identifier)
            self.state = 33
            self.match(JackParser.LPAREN)
            self.state = 34
            self.parameterList()
            self.state = 35
            self.match(JackParser.RPAREN)
            self.state = 36
            self.match(JackParser.LBRACE)
            self.state = 37
            self.subroutineBody()
            self.state = 38
            self.match(JackParser.RETURN)
            self.state = 39
            self.match(JackParser.SEMI)
            self.state = 40
            self.match(JackParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self):
            return self.getToken(JackParser.WS, 0)

        def getRuleIndex(self):
            return JackParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = JackParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameterList)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(JackParser.WS)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubroutineBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JackParser.VarDecContext)
            else:
                return self.getTypedRuleContext(JackParser.VarDecContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JackParser.StatementContext)
            else:
                return self.getTypedRuleContext(JackParser.StatementContext,i)


        def getRuleIndex(self):
            return JackParser.RULE_subroutineBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubroutineBody" ):
                listener.enterSubroutineBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubroutineBody" ):
                listener.exitSubroutineBody(self)




    def subroutineBody(self):

        localctx = JackParser.SubroutineBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_subroutineBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 46
                    self.varDec()
                    pass
                elif token in [16, 20]:
                    self.state = 47
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1114240) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(JackParser.VAR, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(JackParser.Identifier)
            else:
                return self.getToken(JackParser.Identifier, i)

        def SEMI(self):
            return self.getToken(JackParser.SEMI, 0)

        def getRuleIndex(self):
            return JackParser.RULE_varDec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDec" ):
                listener.enterVarDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDec" ):
                listener.exitVarDec(self)




    def varDec(self):

        localctx = JackParser.VarDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(JackParser.VAR)
            self.state = 53
            self.match(JackParser.Identifier)
            self.state = 54
            self.match(JackParser.Identifier)
            self.state = 55
            self.match(JackParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def letStatement(self):
            return self.getTypedRuleContext(JackParser.LetStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(JackParser.WhileStatementContext,0)


        def getRuleIndex(self):
            return JackParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = JackParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.letStatement()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.whileStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(JackParser.LET, 0)

        def Identifier(self):
            return self.getToken(JackParser.Identifier, 0)

        def EQUAL(self):
            return self.getToken(JackParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(JackParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(JackParser.SEMI, 0)

        def getRuleIndex(self):
            return JackParser.RULE_letStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStatement" ):
                listener.enterLetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStatement" ):
                listener.exitLetStatement(self)




    def letStatement(self):

        localctx = JackParser.LetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_letStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(JackParser.LET)
            self.state = 62
            self.match(JackParser.Identifier)
            self.state = 63
            self.match(JackParser.EQUAL)
            self.state = 64
            self.expression()
            self.state = 65
            self.match(JackParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(JackParser.TermContext,0)


        def getRuleIndex(self):
            return JackParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = JackParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringConstant(self):
            return self.getTypedRuleContext(JackParser.StringConstantContext,0)


        def getRuleIndex(self):
            return JackParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = JackParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.stringConstant()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JackParser.Identifier, 0)

        def stringConstant(self):
            return self.getTypedRuleContext(JackParser.StringConstantContext,0)


        def getRuleIndex(self):
            return JackParser.RULE_stringConstant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringConstant" ):
                listener.enterStringConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringConstant" ):
                listener.exitStringConstant(self)




    def stringConstant(self):

        localctx = JackParser.StringConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stringConstant)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(JackParser.Identifier)
                self.state = 72
                self.stringConstant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(JackParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(JackParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(JackParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(JackParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(JackParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(JackParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(JackParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JackParser.StatementContext)
            else:
                return self.getTypedRuleContext(JackParser.StatementContext,i)


        def getRuleIndex(self):
            return JackParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = JackParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(JackParser.WHILE)
            self.state = 77
            self.match(JackParser.LPAREN)
            self.state = 78
            self.expression()
            self.state = 79
            self.match(JackParser.RPAREN)
            self.state = 80
            self.match(JackParser.LBRACE)
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.statement()
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16 or _la==20):
                    break

            self.state = 86
            self.match(JackParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(JackParser.INT, 0)

        def CHAR(self):
            return self.getToken(JackParser.CHAR, 0)

        def BOOLEAN(self):
            return self.getToken(JackParser.BOOLEAN, 0)

        def VOID(self):
            return self.getToken(JackParser.VOID, 0)

        def getRuleIndex(self):
            return JackParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = JackParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





