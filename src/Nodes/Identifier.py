from os import name
from src.Types.TokenTypes import TokenTypes
from src.Node import Node
from src.SymbolTable import SymbolTable
from llvmlite import ir

class Identifier(Node):
    def __init__(self, value: str, expression: Node, type: TokenTypes):
        self.child = expression
        self.type = type
        super().__init__(
            value=value,
            children=[self.child],
            node_type='Identifier'
        )

    def Evaluate(self, symbol_table: SymbolTable):
        i = self.child.Evaluate(symbol_table=symbol_table)
        if self.type is None and symbol_table.get(self.value) is None:
            raise ValueError(f'Variable {self.value} was not declared')      

        if symbol_table.get(self.value) is not None and self.type != TokenTypes.STRING_TYPE:
            ir_alloc = symbol_table.get(self.value).get("pointer", None)
        else:
            ir_alloc = self.builder.alloca(i.type, name=self.value)

        self.builder.store(i, ir_alloc)
        symbol_table.set(self.value, ir_alloc)
        return


