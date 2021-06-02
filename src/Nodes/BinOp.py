from src.Node import Node
from src.Types.TokenTypes import TokenTypes 
from src.Token import Token
from src.SymbolTable import SymbolTable
from llvmlite import ir

OPERATORS = [
    TokenTypes.MINUS, 
    TokenTypes.PLUS, 
    TokenTypes.MULTIPLICATION, 
    TokenTypes.DIVISION, 
    TokenTypes.EQUAL, 
    TokenTypes.LESSER, 
    TokenTypes.GREATER,
    TokenTypes.OR,
    TokenTypes.AND
]

class BinOp(Node):
    def __init__(self, value: Token, child1: Node, child2: Node):
        if value.type not in OPERATORS:
            raise ValueError('BinOp recieved invalid value')

        super().__init__(
            value=value,
            children=[child1, child2],
            node_type='BinOp'
        )
        self.child_1 = child1
        self.child_2 = child2

    
    def Evaluate(self, symbol_table: SymbolTable):
        operand_1_i = self.child_1.Evaluate(symbol_table)
        operand_2_i = self.child_2.Evaluate(symbol_table)

        if self.value.type == TokenTypes.MULTIPLICATION:
            i = self.builder.mul(operand_1_i, operand_2_i)
            return i
        
        elif self.value.type == TokenTypes.DIVISION:
            i = self.builder.sdiv(operand_1_i, operand_2_i)
            return i
        
        elif self.value.type == TokenTypes.MINUS:
            i = self.builder.sub(operand_1_i, operand_2_i)
            return i
        
        elif self.value.type == TokenTypes.GREATER:
            i = self.builder.icmp_signed('>', operand_1_i, operand_2_i)
            return i

        elif self.value.type == TokenTypes.LESSER:
            i = self.builder.icmp_signed('<', operand_1_i, operand_2_i)
            return i
        
        elif self.value.type == TokenTypes.EQUAL:
            i = self.builder.icmp_signed('==', operand_1_i, operand_2_i)
            return i
        
        elif self.value.type == TokenTypes.OR:
            i = self.builder.or_(operand_1_i, operand_2_i)
            return i

        elif self.value.type == TokenTypes.AND:
            i = self.builder.and_(operand_1_i, operand_2_i)
            return i

        else:
            i = self.builder.add(operand_1_i, operand_2_i)
            return i

