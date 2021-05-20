
class SymbolTable:
    def __init__(self):
        self.table = {}

    def get(self, key: str):
        data = self.table.get(key, None)
        if data is None:
            raise ValueError('Undeclared identifier used')
        return data

    def set(self, key: str, type, value):
        self.table[key] = { "value": value, "type": type }
        return
