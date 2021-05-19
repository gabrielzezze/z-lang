from src.Node import Node
from src.SymbolTable import SymbolTable

class FuncOp(Node):
    def __init__(self, value, children, symbol_table: SymbolTable):
        super().__init__(value, children)
        self.symbol_table = symbol_table
    
    def Evaluate(self, symbol_table: SymbolTable):
        pass

