from sly import Lexer
from src.Types.TokenTypes import TokenTypes

class ZTokenizer(Lexer):

    tokens = {
        NUMBER, PLUS, MINUS, MULTIPLICATION,
        DIVISION, PARENTHESIS_OPEN, PARENTHESIS_CLOSE, WHILE, 
        IDENTIFIER, ASSIGNMENT, EOL, PRINT, 
        BLOCK_START, BLOCK_END, EQUAL,
        GREATER, GREATER_EQUAL, LESSER, LESSER_EQUAL, STRING, 
        TRUE, FALSE, STRING_TYPE, INT, IF, ELSE, ELIF, VAR,
        BOOL_TYPE, RETURN, FUNCTION, NOT_EQUAL, OR, AND, ARROW
    }


    ARROW               = r'->'
    NUMBER              = r'\d+'
    PLUS                = r'\+'
    MINUS               = r'-'
    MULTIPLICATION      = r'\*'
    DIVISION            = r'/'
    PARENTHESIS_OPEN    = r'\('
    PARENTHESIS_CLOSE   = r'\)'
    ASSIGNMENT          = r'='
    EOL                 = r'.z'
    BLOCK_START         = r'\{'
    BLOCK_END           = r'\}'
    STRING              = r'''("[^"\\]*(\\.[^"\\]*)*"|'[^'\\]*(\\.[^'\\]*)*')'''
    IDENTIFIER          = r'[a-zA-Z_][a-zA-Z0-9_]*'
    
    IDENTIFIER['While'] = WHILE
    IDENTIFIER['zPrint'] = PRINT
    IDENTIFIER['is_equal_to'] = EQUAL
    IDENTIFIER['is_not_equal_to'] = NOT_EQUAL
    IDENTIFIER['is_greater_than'] = GREATER
    IDENTIFIER['is_greate_equal_than'] = GREATER_EQUAL
    IDENTIFIER['is_lesser_than'] = LESSER
    IDENTIFIER['is_lesser_equal_than'] = LESSER_EQUAL
    IDENTIFIER['charz'] = STRING_TYPE
    IDENTIFIER['true'] = TRUE
    IDENTIFIER['false'] = FALSE
    IDENTIFIER['numz'] = INT
    IDENTIFIER['If'] = IF
    IDENTIFIER['Else'] = ELSE
    IDENTIFIER['Elif'] = ELIF
    IDENTIFIER['var'] = VAR
    IDENTIFIER['bool'] = BOOL_TYPE
    IDENTIFIER['return'] = RETURN
    IDENTIFIER['func'] = FUNCTION
    IDENTIFIER['or'] = OR
    IDENTIFIER['and'] = AND    


    # Ignore new lines char #
    ignore              = ' \t,'
    ignore_newline      = r'\n+'


    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')


    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
