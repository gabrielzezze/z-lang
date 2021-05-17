from enum import Enum

class TokenTypes(Enum):
    IDENTIFER = 0
    FUNCTION = 1
    BLOCK_START = 2
    BLOCK_END = 3
    PRINT = 4
    IF = 5
    ELIF = 6
    ELSE = 7
    WHILE = 8
    VAR = 9
    RETURN = 10
    EQUAL = 11
    NOT_EQUAL = 12
    GREATER = 13
    GREATER_EQUAL = 14
    LESSER = 15
    LESSER_EQUAL = 16
    INT = 17
    BOOL = 18
    STRING = 19
    PARENTHESIS_OPEN = 20
    PARENTHESIS_CLOSE = 21
    EOF = 22
    EOL = 23
    ASSIGNMENT = 24
    NUMBER = 25


