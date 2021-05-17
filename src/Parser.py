from src.Types.TokenTypes import TokenTypes
from src.Tokenizer import Tokenizer

class Parser:
    def __init__(self):
        pass
    
    @staticmethod
    def run(code: str):
        tokenizer = Tokenizer(code=code)
        tokenizer.select_next()
        while tokenizer.actual.type != TokenTypes.EOF:
            print(tokenizer.actual.type)
            print(tokenizer.actual.value)
            print('----------------')
            tokenizer.select_next()
