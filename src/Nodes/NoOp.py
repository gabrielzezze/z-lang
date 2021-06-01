from src.Node import Node
from src.SymbolTable import SymbolTable
from llvmlite import ir

class NoOp(Node):
    def __init__(self):
        super().__init__(
            value='',
            children=[],
            node_type='NoOp'
        )
        pass

    def Evaluate(self, symbol_table):
        i = ir.Constant(ir.IntType(8), 0)
        return None, None, i

