from src.Node import Node
from src.SymbolTable import SymbolTable
from src.Nodes.FuncArguments import FuncArguments

class FuncDeclaration(Node):
    def __init__(self, func_name, statements, args: FuncArguments):
        self.args = args
        self.statements = statements
        super().__init__(
            value=func_name, 
            children=[statements, args],
            node_type='FUNCDEC'
        )

    def Evaluate(self, symbol_table: SymbolTable):
        symbol_table.set_function(key=self.value, value=self)
        return
