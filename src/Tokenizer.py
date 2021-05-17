from src.Token import Token
from src.Types.TokenTypes import TokenTypes

class Tokenizer:
    KEYWORDS = {
        'func':             TokenTypes.FUNCTION, 
        'zPrint':           TokenTypes.PRINT, 
        'If':               TokenTypes.IF,
        'Else':             TokenTypes.ELSE, 
        'Elif':             TokenTypes.ELIF, 
        'While':            TokenTypes.WHILE, 
        'var':              TokenTypes.VAR, 
        'return':           TokenTypes.RETURN, 
        'is_equal_to':      TokenTypes.EQUAL, 
        'is_not_equal_to':  TokenTypes.NOT_EQUAL, 
        'is_greater_than':  TokenTypes.GREATER, 
        'is_greater_equal_than': TokenTypes.GREATER_EQUAL,
        'is_lesser_than':   TokenTypes.LESSER, 
        'is_lesser_equal_than':  TokenTypes.LESSER_EQUAL,
        'numz':             TokenTypes.INT,
        'charz':            TokenTypes.STRING,
        'bool':             TokenTypes.BOOL,
        '.z':               TokenTypes.EOL
    }

    def __init__(self, code: str):
        # Constants
        self.MAX_POSITION = len(code) - 1

        # Code vars
        self.code = code
        self.position = 0
        
        self.parenthesis_opened = 0
        self.brackets_opened = 0
        self.actual = None


    def _check_invalid_position(self):
        if self.position > self.MAX_POSITION:
            if self.position == self.MAX_POSITION + 1:
                return Token(value='', token_type=TokenTypes.EOF)

            raise IndexError('Invalid position @ Tokenize.py - line 17')
        return None

    def _handle_alnum_value(self, value: str):
        token_value = ''
        while value.isalnum() or value in ['_', '.']:
            token_value += value
            self.position += 1
            if self.position >= self.MAX_POSITION + 1:
                break
            value = self.code[self.position]

        token_type = TokenTypes.IDENTIFER
        if token_value in self.KEYWORDS.keys():
            token_type = self.KEYWORDS[token_value]

        return token_type, token_value

    def _handle_parenthesis_value(self, value: str):
        token_type = TokenTypes.PARENTHESIS_OPEN
        if value == ')':
            token_type = TokenTypes.PARENTHESIS_CLOSE
            self.parenthesis_opened -= 1
        else:
            self.parenthesis_opened += 1
        
        self.position += 1
        return token_type, value

    def _handle_brackets_value(self, value: str):
        token_type = TokenTypes.BLOCK_START
        if value == '}':
            token_type = TokenTypes.BLOCK_END
            self.brackets_opened -= 1
        else:
            self.brackets_opened += 1

        self.position += 1
        return token_type, value


    def _handle_number_value(self, value: str):
        token_value = ''
        while value.isdigit():
            token_value += value
            self.position += 1
            if self.position >= self.MAX_POSITION + 1:
                break
            value = self.code[self.position]

        return TokenTypes.NUMBER, int(token_value)


    def _handle_equal_sign_value(self, value: str):
        self.position += 1
        return TokenTypes.ASSIGNMENT, value


    def _ignore_spaces(self):
        while self.code[self.position] == ' ':
            self.position += 1

    def select_next(self):
        eof = self._check_invalid_position()
        if eof is not None:
            self.actual = eof
            return

        token_type = None
        token_value = None

        self._ignore_spaces()
        value = self.code[self.position]

        if value in ['(', ')']:
            token_type, token_value = self._handle_parenthesis_value(value=value)

        elif value in ['{', '}']:
            token_type, token_value = self._handle_brackets_value(value=value)
        
        elif value.isdigit():
            token_type, token_value = self._handle_number_value(value=value)

        elif value == '=':
            token_type, token_value = self._handle_equal_sign_value(value=value)

        elif value.isalnum() or value in ['.']:
            token_type, token_value = self._handle_alnum_value(value=value)
    
        self.actual = Token(
            value=token_value,
            token_type=token_type
        )


