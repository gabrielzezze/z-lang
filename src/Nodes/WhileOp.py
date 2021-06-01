from src.Node import Node
from src.Nodes import Block
from src.SymbolTable import SymbolTable

class WhileOp(Node):
    def __init__(self, child: Block, condition: Node):
        self.condition = condition
        self.child = child
        super().__init__(
            value=condition,
            children=[child, condition],
            node_type='WhileOp'
        )

    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
        _type, condition = self.condition.Evaluate(symbol_table, module, builder, printf)
        while condition:
            self.child.Evaluate(symbol_table, module, builder, printf)
            _type, condition = self.condition.Evaluate(symbol_table, module, builder, printf)

        return
