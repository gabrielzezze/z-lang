from src.Types.TokenTypes import TokenTypes
from src.Node import Node
from src.SymbolTable import SymbolTable

class Identifier(Node):
    def __init__(self, value: str, expression: Node, type: TokenTypes):
        self.child = expression
        self.type = type
        super().__init__(
            value=value,
            children=[self.child],
            node_type='Identifier'
        )

    def Evaluate(self, symbol_table: SymbolTable):
        type, value = self.child.Evaluate(symbol_table=symbol_table)
        if type != None and type != self.type:
            raise ValueError(f'Cannot asscoate {self.type} with {type}')
        elif self.type is None and symbol_table.get(self.value) is None:
            raise ValueError(f'Variable {self.value} was not declared')
        symbol_table.set(self.value, type, value)
        return


