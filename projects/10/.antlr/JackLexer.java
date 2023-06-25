// Generated from c:\Users\wolf9\workspace\nand2tetris\projects\10\Jack.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JackLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CLASS=1, CONSTRUCTOR=2, FUNCTION=3, METHOD=4, FIELD=5, STATIC=6, VAR=7, 
		INT=8, CHAR=9, BOOLEAN=10, VOID=11, TRUE=12, FALSE=13, NULL=14, THIS=15, 
		LET=16, DO=17, IF=18, ELSE=19, WHILE=20, RETURN=21, KEYWORD=22, Identifier=23, 
		LPAREN=24, RPAREN=25, LBRACE=26, RBRACE=27, LBRACK=28, RBRACK=29, SEMI=30, 
		COMMA=31, DOT=32, SYMBOL=33, WS=34, COMMENT=35, LINE_COMMENT=36;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"CLASS", "CONSTRUCTOR", "FUNCTION", "METHOD", "FIELD", "STATIC", "VAR", 
			"INT", "CHAR", "BOOLEAN", "VOID", "TRUE", "FALSE", "NULL", "THIS", "LET", 
			"DO", "IF", "ELSE", "WHILE", "RETURN", "KEYWORD", "Identifier", "JackLetter", 
			"JackLetterOrDigit", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
			"RBRACK", "SEMI", "COMMA", "DOT", "SYMBOL", "WS", "COMMENT", "LINE_COMMENT"
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
			"DOT", "SYMBOL", "WS", "COMMENT", "LINE_COMMENT"
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


	public JackLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Jack.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2&\u010e\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n"+
		"\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3"+
		"\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17"+
		"\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23"+
		"\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\7\30\u00ce\n\30\f\30\16"+
		"\30\u00d1\13\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36"+
		"\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3$\5$\u00ed\n$\3%\6"+
		"%\u00f0\n%\r%\16%\u00f1\3%\3%\3&\3&\3&\3&\7&\u00fa\n&\f&\16&\u00fd\13"+
		"&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\7\'\u0108\n\'\f\'\16\'\u010b\13\'\3\'"+
		"\3\'\3\u00fb\2(\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31"+
		"\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\2\63\2\65\32"+
		"\67\339\34;\35=\36?\37A C!E\"G#I$K%M&\3\2\6\6\2&&C\\aac|\7\2&&\62;C\\"+
		"aac|\5\2\13\f\16\17\"\"\4\2\f\f\17\17\2\u0112\2\3\3\2\2\2\2\5\3\2\2\2"+
		"\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3"+
		"\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2"+
		"\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2"+
		"\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\65\3\2\2\2\2\67\3\2"+
		"\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2"+
		"\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\3O\3\2\2\2\5U"+
		"\3\2\2\2\7a\3\2\2\2\tj\3\2\2\2\13q\3\2\2\2\rw\3\2\2\2\17~\3\2\2\2\21\u0082"+
		"\3\2\2\2\23\u0086\3\2\2\2\25\u008b\3\2\2\2\27\u0093\3\2\2\2\31\u0098\3"+
		"\2\2\2\33\u009d\3\2\2\2\35\u00a3\3\2\2\2\37\u00a8\3\2\2\2!\u00ad\3\2\2"+
		"\2#\u00b1\3\2\2\2%\u00b4\3\2\2\2\'\u00b7\3\2\2\2)\u00bc\3\2\2\2+\u00c2"+
		"\3\2\2\2-\u00c9\3\2\2\2/\u00cb\3\2\2\2\61\u00d2\3\2\2\2\63\u00d4\3\2\2"+
		"\2\65\u00d6\3\2\2\2\67\u00d8\3\2\2\29\u00da\3\2\2\2;\u00dc\3\2\2\2=\u00de"+
		"\3\2\2\2?\u00e0\3\2\2\2A\u00e2\3\2\2\2C\u00e4\3\2\2\2E\u00e6\3\2\2\2G"+
		"\u00ec\3\2\2\2I\u00ef\3\2\2\2K\u00f5\3\2\2\2M\u0103\3\2\2\2OP\7e\2\2P"+
		"Q\7n\2\2QR\7c\2\2RS\7u\2\2ST\7u\2\2T\4\3\2\2\2UV\7e\2\2VW\7q\2\2WX\7p"+
		"\2\2XY\7u\2\2YZ\7v\2\2Z[\7t\2\2[\\\7w\2\2\\]\7e\2\2]^\7v\2\2^_\7q\2\2"+
		"_`\7t\2\2`\6\3\2\2\2ab\7h\2\2bc\7w\2\2cd\7p\2\2de\7e\2\2ef\7v\2\2fg\7"+
		"k\2\2gh\7q\2\2hi\7p\2\2i\b\3\2\2\2jk\7o\2\2kl\7g\2\2lm\7v\2\2mn\7j\2\2"+
		"no\7q\2\2op\7f\2\2p\n\3\2\2\2qr\7h\2\2rs\7k\2\2st\7g\2\2tu\7n\2\2uv\7"+
		"f\2\2v\f\3\2\2\2wx\7u\2\2xy\7v\2\2yz\7c\2\2z{\7v\2\2{|\7k\2\2|}\7e\2\2"+
		"}\16\3\2\2\2~\177\7x\2\2\177\u0080\7c\2\2\u0080\u0081\7t\2\2\u0081\20"+
		"\3\2\2\2\u0082\u0083\7k\2\2\u0083\u0084\7p\2\2\u0084\u0085\7v\2\2\u0085"+
		"\22\3\2\2\2\u0086\u0087\7e\2\2\u0087\u0088\7j\2\2\u0088\u0089\7c\2\2\u0089"+
		"\u008a\7t\2\2\u008a\24\3\2\2\2\u008b\u008c\7d\2\2\u008c\u008d\7q\2\2\u008d"+
		"\u008e\7q\2\2\u008e\u008f\7n\2\2\u008f\u0090\7g\2\2\u0090\u0091\7c\2\2"+
		"\u0091\u0092\7p\2\2\u0092\26\3\2\2\2\u0093\u0094\7x\2\2\u0094\u0095\7"+
		"q\2\2\u0095\u0096\7k\2\2\u0096\u0097\7f\2\2\u0097\30\3\2\2\2\u0098\u0099"+
		"\7v\2\2\u0099\u009a\7t\2\2\u009a\u009b\7w\2\2\u009b\u009c\7g\2\2\u009c"+
		"\32\3\2\2\2\u009d\u009e\7h\2\2\u009e\u009f\7c\2\2\u009f\u00a0\7n\2\2\u00a0"+
		"\u00a1\7u\2\2\u00a1\u00a2\7g\2\2\u00a2\34\3\2\2\2\u00a3\u00a4\7p\2\2\u00a4"+
		"\u00a5\7w\2\2\u00a5\u00a6\7n\2\2\u00a6\u00a7\7n\2\2\u00a7\36\3\2\2\2\u00a8"+
		"\u00a9\7v\2\2\u00a9\u00aa\7j\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac\7u\2\2"+
		"\u00ac \3\2\2\2\u00ad\u00ae\7n\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7v\2"+
		"\2\u00b0\"\3\2\2\2\u00b1\u00b2\7f\2\2\u00b2\u00b3\7q\2\2\u00b3$\3\2\2"+
		"\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7h\2\2\u00b6&\3\2\2\2\u00b7\u00b8\7"+
		"g\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb\7g\2\2\u00bb("+
		"\3\2\2\2\u00bc\u00bd\7y\2\2\u00bd\u00be\7j\2\2\u00be\u00bf\7k\2\2\u00bf"+
		"\u00c0\7n\2\2\u00c0\u00c1\7g\2\2\u00c1*\3\2\2\2\u00c2\u00c3\7t\2\2\u00c3"+
		"\u00c4\7g\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7\7t\2\2"+
		"\u00c7\u00c8\7p\2\2\u00c8,\3\2\2\2\u00c9\u00ca\5\3\2\2\u00ca.\3\2\2\2"+
		"\u00cb\u00cf\5\61\31\2\u00cc\u00ce\5\63\32\2\u00cd\u00cc\3\2\2\2\u00ce"+
		"\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\60\3\2\2"+
		"\2\u00d1\u00cf\3\2\2\2\u00d2\u00d3\t\2\2\2\u00d3\62\3\2\2\2\u00d4\u00d5"+
		"\t\3\2\2\u00d5\64\3\2\2\2\u00d6\u00d7\7*\2\2\u00d7\66\3\2\2\2\u00d8\u00d9"+
		"\7+\2\2\u00d98\3\2\2\2\u00da\u00db\7}\2\2\u00db:\3\2\2\2\u00dc\u00dd\7"+
		"\177\2\2\u00dd<\3\2\2\2\u00de\u00df\7]\2\2\u00df>\3\2\2\2\u00e0\u00e1"+
		"\7_\2\2\u00e1@\3\2\2\2\u00e2\u00e3\7=\2\2\u00e3B\3\2\2\2\u00e4\u00e5\7"+
		".\2\2\u00e5D\3\2\2\2\u00e6\u00e7\7\60\2\2\u00e7F\3\2\2\2\u00e8\u00ed\5"+
		"\65\33\2\u00e9\u00ed\5\67\34\2\u00ea\u00ed\59\35\2\u00eb\u00ed\5;\36\2"+
		"\u00ec\u00e8\3\2\2\2\u00ec\u00e9\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb"+
		"\3\2\2\2\u00edH\3\2\2\2\u00ee\u00f0\t\4\2\2\u00ef\u00ee\3\2\2\2\u00f0"+
		"\u00f1\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2"+
		"\2\2\u00f3\u00f4\b%\2\2\u00f4J\3\2\2\2\u00f5\u00f6\7\61\2\2\u00f6\u00f7"+
		"\7,\2\2\u00f7\u00fb\3\2\2\2\u00f8\u00fa\13\2\2\2\u00f9\u00f8\3\2\2\2\u00fa"+
		"\u00fd\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fe\3\2"+
		"\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\7,\2\2\u00ff\u0100\7\61\2\2\u0100"+
		"\u0101\3\2\2\2\u0101\u0102\b&\2\2\u0102L\3\2\2\2\u0103\u0104\7\61\2\2"+
		"\u0104\u0105\7\61\2\2\u0105\u0109\3\2\2\2\u0106\u0108\n\5\2\2\u0107\u0106"+
		"\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a"+
		"\u010c\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010d\b\'\2\2\u010dN\3\2\2\2"+
		"\b\2\u00cf\u00ec\u00f1\u00fb\u0109\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}