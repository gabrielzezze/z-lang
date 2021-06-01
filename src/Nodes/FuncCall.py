from src.Types.TokenTypes import TokenTypes
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

    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
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

                type, value = self.children[idx].Evaluate(symbol_table, module, builder, printf)
                if arg_type != type:
                    raise ValueError('Agurment given is not the correct type')
                func_symbol_table.set(key, type, value)


            func_key = list(func_args_keys)[0]
            return_type = func_node.args.args[func_key].get('type', None).type
            returned_data = func_node.statements.Evaluate(func_symbol_table, module, builder, printf)

            if returned_data is None:
                raise ValueError(f'Function {func_key} must return {return_type}')
            
            returned_type = returned_data[0]
            returned_value = returned_data[1]

            if returned_type == TokenTypes.INT and return_type != TokenTypes.INT:
                raise ValueError(f'Function {func_key} returned incorrect type')
            elif returned_type == TokenTypes.STRING and return_type != TokenTypes.STRING_TYPE:
                raise ValueError(f'Function {func_key} returned incorrect type')
            elif returned_type in [TokenTypes.FALSE, TokenTypes.TRUE] and return_type != TokenTypes.BOOL_TYPE:
                raise ValueError(f'Function {func_key} returned incorrect type')


            return returned_type, returned_value


        raise ValueError(f'Function {self.value} was not declared')