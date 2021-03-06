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

    def Evaluate(self, symbol_table: SymbolTable):
        condition_i = self.condition.Evaluate(symbol_table=symbol_table)

        i = None
        with self.builder.if_else(condition_i) as (then, otherwise):
            with then:
                true_return_data = self.true_child.Evaluate(symbol_table=symbol_table)
                if true_return_data is not None:
                    i = true_return_data
            
            with otherwise:
                if self.false_child:
                    false_return_data = self.false_child.Evaluate(symbol_table=symbol_table)
                    if false_return_data is not None:
                        i = false_return_data
        
        return i