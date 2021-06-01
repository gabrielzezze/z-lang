from src.Node import Node
from src.SymbolTable import SymbolTable

class Variable(Node):
    def __init__(self, value: str):
        super().__init__(
            value=value,
            children=[],
            node_type='Variable'
        )
        self.value = value

    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
        symbol_table_entry = symbol_table.get(self.value)
        type = symbol_table_entry.get("type", None)
        value = symbol_table_entry.get("value", None)
        return type, value
    
