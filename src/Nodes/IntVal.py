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


    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
        i = ir.Constant(ir.IntType(8), int(self.value.value))
        return TokenTypes.INT, int(self.value.value)
