from src.Types.TokenTypes import TokenTypes
from src.Nodes.Return import ReturnStatement
from src.Node import Node
from src.SymbolTable import SymbolTable
from llvmlite import ir

class FuncCall(Node):
    def __init__(self, value, children):
        super().__init__(
            value=value, 
            children=children,
            node_type='FUNCCALL'
        )

    def Evaluate(self, symbol_table: SymbolTable):
        func_node_data = symbol_table.get_function(self.value)
        if func_node_data is not None:

            func_node = func_node_data.get("value", None)
            if func_node is None:
                raise ValueError('No func node found')

            func_args_keys = func_node.args.args.keys()
            if func_args_keys is None:
                raise ValueError('No arguments node found')

            func_symbol_table = func_node_data.get('symbol_table', None)

            args_values = []
            for arg in self.children:
                i = arg.Evaluate(func_symbol_table)
                args_values.append(i)
            
            ret = self.builder.call(func_node_data.get('pointer', None), args_values)
            return ret
            
        raise ValueError(f'Function {self.value} was not declared')