from src.Node import Node
from src.SymbolTable import SymbolTable

class NoOp(Node):
    def __init__(self):
        super().__init__(
            value='',
            children=[],
            node_type='NoOp'
        )
        pass

    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
        return None, None

