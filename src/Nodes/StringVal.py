from src.Types.TokenTypes import TokenTypes
from src.Node import Node
from src.Token import Token
from src.SymbolTable import SymbolTable

class StringVal(Node):
    def __init__(self, value: Token):
        super().__init__(
            value=value,
            children=[],
            node_type='StringVal'
        )


    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
        return TokenTypes.STRING, str(self.value.value)
