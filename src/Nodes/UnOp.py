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
    

    def Evaluate(self, symbol_table: SymbolTable):
        type, operand, i = self.child.Evaluate(symbol_table)

        if self.value.type == TokenTypes.MINUS:
            new_i = ir.Constant(ir.IntType(8), operand*-1)
            return TokenTypes.INT, operand*-1, new_i

        elif self.value.type == TokenTypes.NOT:
            token_type = TokenTypes.TRUE if not operand else TokenTypes.FALSE
            new_i = ir.Constant(ir.IntType(8), 1 if token_type==TokenTypes.TRUE else 0)
            return token_type, not operand, new_i
        
        else:
            return type, operand, i
        

