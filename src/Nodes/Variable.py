from src.Types.TokenTypes import TokenTypes
from src.Node import Node
from src.SymbolTable import SymbolTable
from llvmlite import ir
class Variable(Node):
    def __init__(self, value: str):
        super().__init__(
            value=value,
            children=[],
            node_type='Variable'
        )
        self.value = value

    def Evaluate(self, symbol_table: SymbolTable):
        symbol_table_entry = symbol_table.get(self.value)
        type = symbol_table_entry.get("type", None)
        value = symbol_table_entry.get("value", None)
        alloc_ptr = symbol_table_entry.get("pointer", None)

        i = self.builder.load(alloc_ptr)
            
        return type, value, i
    
