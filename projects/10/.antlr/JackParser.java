// Generated from c:\Users\wolf9\workspace\nand2tetris\projects\10\Jack.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JackParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CLASS=1, CONSTRUCTOR=2, FUNCTION=3, METHOD=4, FIELD=5, STATIC=6, VAR=7, 
		INT=8, CHAR=9, BOOLEAN=10, VOID=11, TRUE=12, FALSE=13, NULL=14, THIS=15, 
		LET=16, DO=17, IF=18, ELSE=19, WHILE=20, RETURN=21, KEYWORD=22, Identifier=23, 
		LPAREN=24, RPAREN=25, LBRACE=26, RBRACE=27, LBRACK=28, RBRACK=29, SEMI=30, 
		COMMA=31, DOT=32, SYMBOL=33, WS=34, COMMENT=35, LINE_COMMENT=36, EQUAL=37;
	public static final int
		RULE_prog = 0, RULE_subroutineDec = 1, RULE_parameterList = 2, RULE_subroutineBody = 3, 
		RULE_varDec = 4, RULE_statement = 5, RULE_letStatement = 6, RULE_expression = 7, 
		RULE_term = 8, RULE_stringConstant = 9, RULE_whileStatement = 10, RULE_type = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "subroutineDec", "parameterList", "subroutineBody", "varDec", 
			"statement", "letStatement", "expression", "term", "stringConstant", 
			"whileStatement", "type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'constructor'", "'function'", "'method'", "'field'", 
			"'static'", "'var'", "'int'", "'char'", "'boolean'", "'void'", "'true'", 
			"'false'", "'null'", "'this'", "'let'", "'do'", "'if'", "'else'", "'while'", 
			"'return'", null, null, "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
			"','", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CLASS", "CONSTRUCTOR", "FUNCTION", "METHOD", "FIELD", "STATIC", 
			"VAR", "INT", "CHAR", "BOOLEAN", "VOID", "TRUE", "FALSE", "NULL", "THIS", 
			"LET", "DO", "IF", "ELSE", "WHILE", "RETURN", "KEYWORD", "Identifier", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", 
			"DOT", "SYMBOL", "WS", "COMMENT", "LINE_COMMENT", "EQUAL"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Jack.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public JackParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(JackParser.CLASS, 0); }
		public TerminalNode Identifier() { return getToken(JackParser.Identifier, 0); }
		public List<TerminalNode> SYMBOL() { return getTokens(JackParser.SYMBOL); }
		public TerminalNode SYMBOL(int i) {
			return getToken(JackParser.SYMBOL, i);
		}
		public SubroutineDecContext subroutineDec() {
			return getRuleContext(SubroutineDecContext.class,0);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			match(CLASS);
			setState(25);
			match(Identifier);
			setState(26);
			match(SYMBOL);
			setState(27);
			subroutineDec();
			setState(28);
			match(SYMBOL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubroutineDecContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(JackParser.FUNCTION, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode Identifier() { return getToken(JackParser.Identifier, 0); }
		public TerminalNode LPAREN() { return getToken(JackParser.LPAREN, 0); }
		public ParameterListContext parameterList() {
			return getRuleContext(ParameterListContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(JackParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(JackParser.LBRACE, 0); }
		public SubroutineBodyContext subroutineBody() {
			return getRuleContext(SubroutineBodyContext.class,0);
		}
		public TerminalNode RETURN() { return getToken(JackParser.RETURN, 0); }
		public TerminalNode SEMI() { return getToken(JackParser.SEMI, 0); }
		public TerminalNode RBRACE() { return getToken(JackParser.RBRACE, 0); }
		public SubroutineDecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subroutineDec; }
	}

	public final SubroutineDecContext subroutineDec() throws RecognitionException {
		SubroutineDecContext _localctx = new SubroutineDecContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_subroutineDec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			match(FUNCTION);
			setState(31);
			type();
			setState(32);
			match(Identifier);
			setState(33);
			match(LPAREN);
			setState(34);
			parameterList();
			setState(35);
			match(RPAREN);
			setState(36);
			match(LBRACE);
			setState(37);
			subroutineBody();
			setState(38);
			match(RETURN);
			setState(39);
			match(SEMI);
			setState(40);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParameterListContext extends ParserRuleContext {
		public TerminalNode WS() { return getToken(JackParser.WS, 0); }
		public ParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterList; }
	}

	public final ParameterListContext parameterList() throws RecognitionException {
		ParameterListContext _localctx = new ParameterListContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_parameterList);
		try {
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case WS:
				enterOuterAlt(_localctx, 1);
				{
				setState(42);
				match(WS);
				}
				break;
			case RPAREN:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubroutineBodyContext extends ParserRuleContext {
		public List<VarDecContext> varDec() {
			return getRuleContexts(VarDecContext.class);
		}
		public VarDecContext varDec(int i) {
			return getRuleContext(VarDecContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public SubroutineBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subroutineBody; }
	}

	public final SubroutineBodyContext subroutineBody() throws RecognitionException {
		SubroutineBodyContext _localctx = new SubroutineBodyContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_subroutineBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(48);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case VAR:
					{
					setState(46);
					varDec();
					}
					break;
				case LET:
				case WHILE:
					{
					setState(47);
					statement();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(50); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << LET) | (1L << WHILE))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarDecContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(JackParser.VAR, 0); }
		public List<TerminalNode> Identifier() { return getTokens(JackParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(JackParser.Identifier, i);
		}
		public TerminalNode SEMI() { return getToken(JackParser.SEMI, 0); }
		public VarDecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDec; }
	}

	public final VarDecContext varDec() throws RecognitionException {
		VarDecContext _localctx = new VarDecContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_varDec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			match(VAR);
			setState(53);
			match(Identifier);
			setState(54);
			match(Identifier);
			setState(55);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public LetStatementContext letStatement() {
			return getRuleContext(LetStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_statement);
		try {
			setState(59);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LET:
				enterOuterAlt(_localctx, 1);
				{
				setState(57);
				letStatement();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(58);
				whileStatement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LetStatementContext extends ParserRuleContext {
		public TerminalNode LET() { return getToken(JackParser.LET, 0); }
		public TerminalNode Identifier() { return getToken(JackParser.Identifier, 0); }
		public TerminalNode EQUAL() { return getToken(JackParser.EQUAL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(JackParser.SEMI, 0); }
		public LetStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letStatement; }
	}

	public final LetStatementContext letStatement() throws RecognitionException {
		LetStatementContext _localctx = new LetStatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_letStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(LET);
			setState(62);
			match(Identifier);
			setState(63);
			match(EQUAL);
			setState(64);
			expression();
			setState(65);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			term();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public StringConstantContext stringConstant() {
			return getRuleContext(StringConstantContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_term);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			stringConstant();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StringConstantContext extends ParserRuleContext {
		public TerminalNode Identifier() { return getToken(JackParser.Identifier, 0); }
		public StringConstantContext stringConstant() {
			return getRuleContext(StringConstantContext.class,0);
		}
		public StringConstantContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringConstant; }
	}

	public final StringConstantContext stringConstant() throws RecognitionException {
		StringConstantContext _localctx = new StringConstantContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_stringConstant);
		try {
			setState(74);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(71);
				match(Identifier);
				setState(72);
				stringConstant();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(73);
				match(Identifier);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhileStatementContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(JackParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(JackParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(JackParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(JackParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(JackParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_whileStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(WHILE);
			setState(77);
			match(LPAREN);
			setState(78);
			expression();
			setState(79);
			match(RPAREN);
			setState(80);
			match(LBRACE);
			setState(82); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(81);
				statement();
				}
				}
				setState(84); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LET || _la==WHILE );
			setState(86);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(JackParser.INT, 0); }
		public TerminalNode CHAR() { return getToken(JackParser.CHAR, 0); }
		public TerminalNode BOOLEAN() { return getToken(JackParser.BOOLEAN, 0); }
		public TerminalNode VOID() { return getToken(JackParser.VOID, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << CHAR) | (1L << BOOLEAN) | (1L << VOID))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\']\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\4\r\t\r\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\4\3\4\5\4/\n\4\3\5\3\5\6\5\63\n\5\r\5\16\5\64\3\6\3"+
		"\6\3\6\3\6\3\6\3\7\3\7\5\7>\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3"+
		"\n\3\13\3\13\3\13\5\13M\n\13\3\f\3\f\3\f\3\f\3\f\3\f\6\fU\n\f\r\f\16\f"+
		"V\3\f\3\f\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\3\3\2\n\r"+
		"\2V\2\32\3\2\2\2\4 \3\2\2\2\6.\3\2\2\2\b\62\3\2\2\2\n\66\3\2\2\2\f=\3"+
		"\2\2\2\16?\3\2\2\2\20E\3\2\2\2\22G\3\2\2\2\24L\3\2\2\2\26N\3\2\2\2\30"+
		"Z\3\2\2\2\32\33\7\3\2\2\33\34\7\31\2\2\34\35\7#\2\2\35\36\5\4\3\2\36\37"+
		"\7#\2\2\37\3\3\2\2\2 !\7\5\2\2!\"\5\30\r\2\"#\7\31\2\2#$\7\32\2\2$%\5"+
		"\6\4\2%&\7\33\2\2&\'\7\34\2\2\'(\5\b\5\2()\7\27\2\2)*\7 \2\2*+\7\35\2"+
		"\2+\5\3\2\2\2,/\7$\2\2-/\3\2\2\2.,\3\2\2\2.-\3\2\2\2/\7\3\2\2\2\60\63"+
		"\5\n\6\2\61\63\5\f\7\2\62\60\3\2\2\2\62\61\3\2\2\2\63\64\3\2\2\2\64\62"+
		"\3\2\2\2\64\65\3\2\2\2\65\t\3\2\2\2\66\67\7\t\2\2\678\7\31\2\289\7\31"+
		"\2\29:\7 \2\2:\13\3\2\2\2;>\5\16\b\2<>\5\26\f\2=;\3\2\2\2=<\3\2\2\2>\r"+
		"\3\2\2\2?@\7\22\2\2@A\7\31\2\2AB\7\'\2\2BC\5\20\t\2CD\7 \2\2D\17\3\2\2"+
		"\2EF\5\22\n\2F\21\3\2\2\2GH\5\24\13\2H\23\3\2\2\2IJ\7\31\2\2JM\5\24\13"+
		"\2KM\7\31\2\2LI\3\2\2\2LK\3\2\2\2M\25\3\2\2\2NO\7\26\2\2OP\7\32\2\2PQ"+
		"\5\20\t\2QR\7\33\2\2RT\7\34\2\2SU\5\f\7\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2"+
		"\2VW\3\2\2\2WX\3\2\2\2XY\7\35\2\2Y\27\3\2\2\2Z[\t\2\2\2[\31\3\2\2\2\b"+
		".\62\64=LV";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}