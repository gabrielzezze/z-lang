from src.Nodes.Return import ReturnStatement
from src.Node import Node
from src.SymbolTable import SymbolTable

class Block(Node):
    def __init__(self):
        super().__init__(
            value='',
            children=[],
            node_type='Block'
        )
        self.children = []
    
    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
        for child in self.children:
            return_data = child.Evaluate(symbol_table, module, builder, printf)
            if type(child) == ReturnStatement:
                return return_data