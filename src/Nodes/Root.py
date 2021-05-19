from src.Node import Node
from src.SymbolTable import SymbolTable

class Root(Node):
    def __init__(self, children):
        super().__init__(
            value='root',
            children=children
        )
    
    def Evaluate(self, symbol_table: SymbolTable):
        for child in self.children:
            child.Evaluate(symbol_table=symbol_table)
