from src.Types.TokenTypes import TokenTypes
from src.Node import Node
from src.Token import Token
from src.SymbolTable import SymbolTable
from src.Types.VariableTypes import VariableTypes

class IntVal(Node):
    def __init__(self, value: Token):
        super().__init__(
            value=value,
            children=[]
        )


    def Evaluate(self, symbol_table: SymbolTable):
        return TokenTypes.INT, int(self.value.value)
