from src.Types.TokenTypes import TokenTypes

class SymbolTable:
    def __init__(self):
        self.table = {}
        self.functions = {}

    def get(self, key: str):
        data = self.table.get(key, None)
        if data is None:
            return None
        return data

    def set(self, key: str, pointer):
        self.table[key] = { "pointer": pointer }
        return

    
    def get_function(self, key: str):
        data = self.functions.get(key, None)
        if data is None:
            return None
        return data

    def set_function(self, key: str, value, func_symbol_table, func_i):
        self.functions[key] = { "value": value, "type": TokenTypes.FUNCTION, "symbol_table": func_symbol_table, "pointer": func_i}
        return
