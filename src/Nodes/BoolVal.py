from src.Types.TokenTypes import TokenTypes
from src.Node import Node
from src.Token import Token
from src.SymbolTable import SymbolTable
from llvmlite import ir

class BoolVal(Node):

    def __init__(self, value: Token):
        self.value = value
        super().__init__(
            value=value,
            children=[],
            node_type='BoolVal'
        )

    def Evaluate(self, symbol_table: SymbolTable):
        i = ir.Constant(ir.IntType(1), 1 if self.value.value else 0)
        return i
