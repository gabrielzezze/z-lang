from src.Nodes.Return import ReturnStatement
from src.Node import Node
from src.SymbolTable import SymbolTable


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
            func_symbol_table = SymbolTable()
            func_symbol_table.functions = symbol_table.functions

            func_node = func_node_data.get("value", None)
            if func_node is None:
                raise ValueError('No func node found')

            func_args_keys = func_node.args.args.keys()
            if func_args_keys is None:
                raise ValueError('No arguments node found')

            for idx in range(0, len(func_args_keys)-1):
                key = list(func_args_keys)[idx+1]
                arg_type = func_node.args.args[key].get('type', None)

                type, value = self.children[idx].Evaluate(symbol_table)
                if arg_type != type:
                    raise ValueError('Agurment given is not the correct type')
                func_symbol_table.set(key, type, value)


            returned_data = func_node.statements.Evaluate(symbol_table=func_symbol_table)
            return returned_data


        raise ValueError(f'Function {self.value} was not declared')