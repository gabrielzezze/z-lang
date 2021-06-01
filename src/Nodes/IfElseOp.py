from src.Node import Node
from src.Nodes import Block
from src.SymbolTable import SymbolTable

class IfElseOp(Node):
    def __init__(self, true_child: Node, false_child: Node, condition: Node):
        self.condition = condition
        self.true_child = true_child
        self.false_child = false_child
        super().__init__(
            value=condition,
            children=[true_child, false_child, condition],
            node_type='IfElseOp'
        )

    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
        _type, condition = self.condition.Evaluate(symbol_table, module, builder, printf)
        if condition:
            return_data = self.true_child.Evaluate(symbol_table, module, builder, printf)
            return return_data
        else:
            if self.false_child is not None:
                return_data = self.false_child.Evaluate(symbol_table, module, builder, printf)
                return return_data
        return