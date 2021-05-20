from src.Types.TokenTypes import TokenTypes
from src.Node import Node
from src.Token import Token
from src.SymbolTable import SymbolTable

class IntVal(Node):
    def __init__(self, value: Token):
        super().__init__(
            value=value,
            children=[],
            node_type='IntVal'
        )


    def Evaluate(self, symbol_table: SymbolTable):
        return TokenTypes.INT, int(self.value.value)
