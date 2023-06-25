grammar Jack;
import CommonLexerRules;

prog
    :   'class' Identifier SYMBOL
            subroutineDec
        SYMBOL
    ;

subroutineDec
    :   'function' type Identifier '(' parameterList ')' '{'
            subroutineBody
            'return' ';'
        '}'
    ;

parameterList
    : WS
    |
    ;

subroutineBody
    :   (varDec | statement)+
    ;

varDec: VAR Identifier Identifier SEMI;

statement
    : letStatement
    | whileStatement
   // | doStatement
   // | returnStatement
    ;

letStatement
    : LET Identifier EQUAL expression SEMI
    ;

expression
    : term
    ;

term
    : stringConstant
    ;

stringConstant
    : Identifier stringConstant
    | Identifier
    ;

whileStatement
    : WHILE LPAREN expression RPAREN LBRACE (statement)+ RBRACE
    ;

type
    : INT
    | CHAR
    | BOOLEAN
    | VOID
    ;

// LEXER

CLASS       : 'class';
CONSTRUCTOR : 'constructor';
FUNCTION    : 'function';
METHOD      : 'method';
FIELD       : 'field';
STATIC      : 'static';
VAR         : 'var';
INT         : 'int';
CHAR        : 'char';
BOOLEAN     : 'boolean';
VOID        : 'void';
TRUE        : 'true';
FALSE       : 'false';
NULL        : 'null';
THIS        : 'this';
LET         : 'let';
DO          : 'do';
IF          : 'if';
ELSE        : 'else';
WHILE       : 'while';
RETURN      : 'return';

KEYWORD
    : CLASS
    ;

Identifier
	:	JackLetter JackLetterOrDigit*
	;

fragment
JackLetter
	:	[a-zA-Z$_]
	;

fragment
JackLetterOrDigit
	:	[a-zA-Z0-9$_]
	;

// Separators
LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LBRACK : '[';
RBRACK : ']';
SEMI   : ';';
COMMA  : ',';
DOT    : '.';

SYMBOL
    :   LPAREN
    |   RPAREN
    |   LBRACE
    |   RBRACE
    ;