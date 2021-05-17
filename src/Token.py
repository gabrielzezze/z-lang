from src.Types.TokenTypes import TokenTypes

class Token():
    def __init__(self, token_type: TokenTypes, value):
        self.type = token_type
        self.value = value
