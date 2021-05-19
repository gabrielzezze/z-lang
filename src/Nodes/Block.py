from src.Node import Node
from src.SymbolTable import SymbolTable

class Block(Node):
    def __init__(self):
        super().__init__(
            value='',
            children=[]
        )
        self.children = []
    
    def Evaluate(self, symbol_table: SymbolTable):
        for child in self.children:
            child.Evaluate(symbol_table)
