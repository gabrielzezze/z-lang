from src.Types.TokenTypes import TokenTypes
from src.Node import Node
from src.Token import Token
from src.SymbolTable import SymbolTable
from llvmlite import ir
class IntVal(Node):
    def __init__(self, value: Token):
        super().__init__(
            value=value,
            children=[],
            node_type='IntVal'
        )


    def Evaluate(self, symbol_table: SymbolTable):
        num = int(self.value.value)
        i = ir.Constant(ir.IntType(8), num)
        return i
