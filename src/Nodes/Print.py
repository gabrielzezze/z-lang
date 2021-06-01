from src.Node import Node
from src.SymbolTable import SymbolTable

class Print(Node):
    def __init__(self, expression: Node):
        self.expression = expression
        super().__init__(
            value=None,
            children=expression,
            node_type='Print'
        )

    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
        _type, result = self.expression.Evaluate(symbol_table, module, builder, printf)
        print(result)
