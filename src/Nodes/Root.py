from src.Node import Node
from src.SymbolTable import SymbolTable

class Root(Node):
    def __init__(self):
        super().__init__(
            value='root',
            children=[],
            node_type='ROOT'
        )

    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
        for child in self.children:
            child.Evaluate(symbol_table, module, builder, printf)
