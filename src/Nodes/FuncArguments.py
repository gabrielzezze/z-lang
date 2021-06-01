from src.Node import Node
from src.SymbolTable import SymbolTable

class FuncArguments(Node):
    def __init__(self, func_name, return_type):
        self.args = {
            func_name: { "value": None, "type": return_type } 
        }
        super().__init__(
            value=func_name, 
            children=[],
            node_type='FUNCARG'
        )
    
    def add_argument(self, name, type):
        if self.args.get(name, None) is None:
            self.args[name] = { "type": type, "value": None }
        else:
            raise ValueError(f'Argument {name} was already defined')

    def get_argument(self, key):
        data = self.args.get(key, None)
        if data is None:
            raise ValueError('Undeclared arg')
        
        return data

    def set_argument(self, key: str, value):
        pass

    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
        pass