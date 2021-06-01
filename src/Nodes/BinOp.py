from src.Node import Node
from src.Types.TokenTypes import TokenTypes 
from src.Token import Token
from src.SymbolTable import SymbolTable

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

    
    def Evaluate(self, symbol_table: SymbolTable, builder, module, printf):
        type_operand_1, operand_1 = self.child_1.Evaluate(symbol_table, module, builder, printf)
        type_operand_2, operand_2 = self.child_2.Evaluate(symbol_table, module, builder, printf)
        if self.value.type == TokenTypes.MULTIPLICATION:
            if type_operand_1 != TokenTypes.INT or type_operand_2 != TokenTypes.INT:
                raise TypeError('[SEMANTIC ERROR] Tried Multiplication op between non INT values')
            return TokenTypes.INT, operand_1*operand_2
        
        elif self.value.type == TokenTypes.DIVISION:
            if type_operand_1 != TokenTypes.INT or type_operand_2 != TokenTypes.INT:
                raise TypeError('[SEMANTIC ERROR] Tried Division op between non INT values')
            return TokenTypes.INT, int(operand_1/operand_2)
        
        elif self.value.type == TokenTypes.MINUS:
            if type_operand_1 != TokenTypes.INT or type_operand_2 != TokenTypes.INT:
                raise TypeError('[SEMANTIC ERROR] Tried Minus op between non INT values')
            return TokenTypes.INT, operand_1-operand_2
        
        elif self.value.type == TokenTypes.GREATER:
            if type_operand_1 != TokenTypes.INT or type_operand_2 != TokenTypes.INT:
                raise TypeError('[SEMANTIC ERROR] Tried Greater op between non INT values')

            result = operand_1 > operand_2
            type = TokenTypes.FALSE
            if result:
                type = TokenTypes.TRUE
            return type, result

        elif self.value.type == TokenTypes.LESSER:
            if type_operand_1 != TokenTypes.INT or type_operand_2 != TokenTypes.INT:
                raise TypeError('[SEMANTIC ERROR] Tried Lesser op between non INT values')

            result = operand_1 < operand_2
            type = TokenTypes.FALSE
            if result:
                type = TokenTypes.TRUE
            return type, result
        
        elif self.value.type == TokenTypes.EQUAL:
            result = operand_1 == operand_2
            type = TokenTypes.FALSE
            if result:
                type = TokenTypes.TRUE
            return type, result
        
        elif self.value.type == TokenTypes.OR:
            result = operand_1 or operand_2
            type = TokenTypes.FALSE
            if result:
                type = TokenTypes.TRUE
            return type, result

        elif self.value.type == TokenTypes.AND:
            result = operand_1 and operand_2
            type = TokenTypes.FALSE
            if result:
                type = TokenTypes.TRUE
            return type, result

        else:
            if type_operand_1 != TokenTypes.INT or type_operand_2 != TokenTypes.INT:
                raise TypeError('[SEMANTIC ERROR] Tried Add op between non INT values')
            return TokenTypes.INT, operand_1+operand_2

