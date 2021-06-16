from src.Types.TokenTypes import TokenTypes
from src.Node import Node
from src.Token import Token
from src.SymbolTable import SymbolTable
from llvmlite import ir

class StringVal(Node):
    def __init__(self, value: Token):
        super().__init__(
            value=value,
            children=[],
            node_type='StringVal'
        )


    def Evaluate(self, symbol_table: SymbolTable):
        if len(self.value.value) < 64:
            self.value.value = self.value.value + (" "*(64-len(self.value.value)))
        elif len(self.value.value) > 64:
            self.value.value = self.value.value[0:63]
        
        i = ir.Constant(ir.ArrayType(ir.IntType(8), 64), bytearray(self.value.value.encode("utf8")))
        return i
