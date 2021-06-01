from src.Node import Node
from src.SymbolTable import SymbolTable

class ReturnStatement(Node):
    def __init__(self, expression):
        self.expression = expression
        super().__init__(
            value='',
            children=[expression],
            node_type='RETURN'
        )

    def Evaluate(self, symbol_table: SymbolTable):
        type, value = self.expression.Evaluate(symbol_table)
        return type, value