from src.Node import Node
from src.SymbolTable import SymbolTable
from llvmlite import ir
class Print(Node):
    def __init__(self, expression: Node):
        self.expression = expression
        super().__init__(
            value=None,
            children=expression,
            node_type='Print'
        )

    def Evaluate(self, symbol_table: SymbolTable):
        i = self.expression.Evaluate(symbol_table=symbol_table)
        
        # Declare argument list
        voidptr_ty = ir.IntType(8).as_pointer()
        
        fmt_arg = self.builder.bitcast(self.global_fmt, voidptr_ty)

        # Call Print Function
        self.builder.call(self.printf, [fmt_arg, i])
        