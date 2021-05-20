from src.Types.TokenTypes import TokenTypes
from src.Node import Node
from src.Token import Token
from src.SymbolTable import SymbolTable

class ReturnStatement(Node):
    def __init__(self, expression: Node):
        self.expression = expression
        super().__init__(
            value='',
            children=[expression],
            node_type='ReturnStatement'
        )


    def Evaluate(self, symbol_table: SymbolTable):
        return self.expression.Evaluate(symbol_table)
