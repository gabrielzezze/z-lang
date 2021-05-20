from src.Types.TokenTypes import TokenTypes
from src.Node import Node
from src.Token import Token
from src.SymbolTable import SymbolTable

class BoolVal(Node):

    def __init__(self, value: Token):
        self.value = value
        super().__init__(
            value=value,
            children=[],
            node_type='BoolVal'
        )

    def Evaluate(self, symbol_table: SymbolTable):
        type = TokenTypes.TRUE
        if not self.value.value:
            type = TokenTypes.FALSE
        return type, self.value.value
