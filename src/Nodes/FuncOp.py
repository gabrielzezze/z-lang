from src.Node import Node
from src.SymbolTable import SymbolTable

class FuncOp(Node):
    def __init__(self, value, child_block, arguments):
        super().__init__(value, children=[child_block], node_type='FuncOp')
    
    def Evaluate(self, symbol_table: SymbolTable):
        pass
