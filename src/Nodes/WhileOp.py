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

    def Evaluate(self, symbol_table: SymbolTable):

        while_entry = self.builder.append_basic_block(name=f'while_{self.id}')
        while_exit = self.builder.append_basic_block(name=f'exit_while_{self.id}')
        _type, condition, condition_i = self.condition.Evaluate(symbol_table=symbol_table)
        self.builder.cbranch(condition_i, while_entry, while_exit)

        self.builder.position_at_start(while_entry)
        self.child.Evaluate(symbol_table=symbol_table)
        _type, condition, condition_i = self.condition.Evaluate(symbol_table)
        self.builder.cbranch(condition_i, while_entry, while_exit)
        self.builder.position_at_start(while_exit)

        return
