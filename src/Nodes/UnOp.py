from src.Node import Node
from src.Token import Token
from src.Types.TokenTypes import TokenTypes 
from src.SymbolTable import SymbolTable

UNARY_OPERATORS = [TokenTypes.PLUS, TokenTypes.MINUS]

class UnOp(Node):
    def __init__(self, value: Token, child: Node):
        if value.type not in UNARY_OPERATORS:
            raise ValueError('UnOp node recieved invalid value')
            
        super().__init__(value=value, children=[child], node_type='UnOp')
        self.child = child
    

    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
        operand = self.child.Evaluate(symbol_table, module, builder, printf)

        if self.value.type == TokenTypes.MINUS:
            return operand*-1
        elif self.value.type == TokenTypes.NOT:
            return not operand
        else:
            return operand
        

