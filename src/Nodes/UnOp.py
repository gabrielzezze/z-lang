from src.Node import Node
from src.Token import Token
from src.Types.TokenTypes import TokenTypes 
from src.SymbolTable import SymbolTable
from llvmlite import ir

UNARY_OPERATORS = [TokenTypes.PLUS, TokenTypes.MINUS]

class UnOp(Node):
    def __init__(self, value: Token, child: Node):
        if value.type not in UNARY_OPERATORS:
            raise ValueError('UnOp node recieved invalid value')
            
        super().__init__(value=value, children=[child], node_type='UnOp')
        self.child = child
    

    def Evaluate(self, symbol_table: SymbolTable):
        i = self.child.Evaluate(symbol_table)

        if self.value.type == TokenTypes.MINUS:
            return self.builder.neg(i)

        elif self.value.type == TokenTypes.NOT:
            return self.builder.not_(i)
        
        else:
            return i
        

