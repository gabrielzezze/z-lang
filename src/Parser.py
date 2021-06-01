from sly import Parser
from src.Nodes.Root import Root
from src.Nodes.FuncCall import FuncCall
from src.SymbolTable import SymbolTable
from src.Token import Token
from src.Types.TokenTypes import TokenTypes
from src.Tokenizer import ZTokenizer
from src.Nodes.BinOp import BinOp
from src.Nodes.UnOp import UnOp
from src.Nodes.NoOp import NoOp
from src.Nodes.IntVal import IntVal
from src.Nodes.BoolVal import BoolVal
from src.Nodes.StringVal import StringVal
from src.Nodes.Variable import Variable
from src.Nodes.Identifier import Identifier
from src.Nodes.Print import Print
from src.Nodes.Block import Block
from src.Nodes.IfElseOp import IfElseOp
from src.Nodes.WhileOp import WhileOp
from src.Nodes.FuncArguments import FuncArguments
from src.Nodes.FuncDeclaration import FuncDeclaration
from src.Nodes.Return import ReturnStatement

class ZParser(Parser):
    tokens = ZTokenizer.tokens

    debugfile = 'test_parser.out'

    precedence = (
        ('left', PLUS, MINUS),
        ('left', MULTIPLICATION, DIVISION),
        ('right', UMINUS, UPLUS),
    )

    def __init__(self):
        self.names = {}

    @_(
        '{ function }'
    )
    def func_def(self, p):
        root_node = Root()
        children = []
        for func in p._1_repeat:
            children.append(func[0])

        root_node.children = children
        return root_node


    @_(
        'FUNCTION IDENTIFIER PARENTHESIS_OPEN { argument } PARENTHESIS_CLOSE block EOL'
    )
    def function(self, p):
        values = p._slice
        node = NoOp()

        if values[0].type == 'FUNCTION':
            func_args = FuncArguments(func_name=values[1].value)
            if len(values) > 6:
                for arg in p.argument:
                    func_args.add_argument(name=arg.value, type=arg.type)

            return FuncDeclaration(func_name=values[1].value, statements=p.block, args=func_args)
        
        return node


    @_(
        'INT IDENTIFIER',
        'STRING_TYPE IDENTIFIER',
        'BOOL_TYPE IDENTIFIER'
    )
    def argument(self, p):
        values = p._slice

        token = None
        if values[0].type == 'INT':
            token = Token(token_type=TokenTypes.INT, value=values[1].value)

        elif values[0].type == 'STRING_TYPE':
            token = Token(token_type=TokenTypes.STRING_TYPE, value=values[1].value)
        
        elif values[0].type == 'BOOL_TYPE':
            token = Token(token_type=TokenTypes.BOOL_TYPE, value=values[1].value)
        

        return token



    @_(
        'BLOCK_START BLOCK_END',
        'BLOCK_START { command } BLOCK_END',
    )
    def block(self, p):
        values = p._slice
        node = NoOp()
        if values[0].type == 'BLOCK_START' and len(values) > 2:
            node = Block()
            for cmd in p.command:
                node.children.append(cmd)
        
        elif values[0].type == 'BLOCK_START' and len(values) == 2:
            node = Block()
            node.children.append(NoOp())

        return node

    @_(
        'EOL',
        'PRINT PARENTHESIS_OPEN or_expression PARENTHESIS_CLOSE EOL',
        'WHILE PARENTHESIS_OPEN or_expression PARENTHESIS_CLOSE command',
        
        'IF PARENTHESIS_OPEN or_expression PARENTHESIS_CLOSE command elif_statement EOL',
        'IF PARENTHESIS_OPEN or_expression PARENTHESIS_CLOSE command EOL',
        
        'VAR IDENTIFIER ARROW INT EOL',
        'VAR IDENTIFIER ARROW INT ASSIGNMENT func_call EOL',
        'VAR IDENTIFIER ARROW INT ASSIGNMENT or_expression EOL',
        
        'VAR IDENTIFIER ARROW STRING_TYPE EOL',
        'VAR IDENTIFIER ARROW STRING_TYPE ASSIGNMENT func_call EOL',
        'VAR IDENTIFIER ARROW STRING_TYPE ASSIGNMENT or_expression EOL',
        
        'VAR IDENTIFIER ARROW BOOL_TYPE EOL',
        'VAR IDENTIFIER ARROW BOOL_TYPE ASSIGNMENT func_call EOL',
        'VAR IDENTIFIER ARROW BOOL_TYPE ASSIGNMENT or_expression EOL',
        
        'IDENTIFIER ASSIGNMENT or_expression EOL',
        'IDENTIFIER ASSIGNMENT func_call EOL',

        'func_call',

        'block',

        'RETURN or_expression EOL'
    )
    def command(self, p):
        values = p._slice
        type = values[0].type


        node = None
        if type == 'EOL':
            node = NoOp()

        elif type == 'PRINT':
            node = Print(expression=p.or_expression)

        elif type == 'WHILE':
            node = WhileOp(child=p.command, condition=p.or_expression)
        
        elif type == 'IF':
            if len(values) == 6:
                node = IfElseOp(true_child=p.command, false_child=None, condition=p.or_expression)
            elif len(values) > 6:
                node = IfElseOp(true_child=p.command, false_child=p.elif_statement, condition=p.or_expression)
        
        elif type == 'VAR':
            expression = NoOp()
            if len(values) > 5:
                if values[5].type == 'or_expression':
                    expression = p.or_expression
                else:
                    expression = p.func_call

            type = TokenTypes.STRING_TYPE
            if values[3].type == 'INT':
                type = TokenTypes.INT
            elif values[3].type == 'BOOL_TYPE':
                type = TokenTypes.BOOL_TYPE
            
            node = Identifier(value=values[1].value, expression=expression, type=type)
        
        elif type == 'IDENTIFIER':
            if values[5].type == 'or_expression':
                expression = p.or_expression
            else:
                expression = p.func_call
                
            node = Identifier(value=values[0].value, expression=p.or_expression)

        elif type == 'block':
            node = p.block
        
        elif type == 'RETURN':
            node = ReturnStatement(expression=p.or_expression)

        return node

    @_(
        'IDENTIFIER PARENTHESIS_OPEN { or_expression } PARENTHESIS_CLOSE'
    )
    def func_call(self, p):
        args = []
        node = NoOp()
        for arg in p.or_expression:
            args.append(arg)
        
        node = FuncCall(value=p._slice[0].value, children=args)
        return node


    @_(
        'ELIF PARENTHESIS_OPEN or_expression PARENTHESIS_CLOSE command elif_statement',
        'ELIF PARENTHESIS_OPEN or_expression PARENTHESIS_CLOSE command',
        'else_statement'
    )
    def elif_statement(self, p):
        values = p._slice

        node = NoOp()
        if values[0].type == "ELIF" and len(values) > 4:
            node = IfElseOp(condition=p.or_expression, true_child=p.command, false_child=p.elif_statement)
        
        elif values[0].type == "ELIF" and len(values) == 4:
            node = IfElseOp(condition=p.or_expression, true_child=p.command, false_child=None)

        elif values[0].type == "else_statement":
            node = p.else_statement

        return node


    @_(
        'ELSE command'
    )
    def else_statement(self, p):
        values = p._slice
        
        node = NoOp()
        if values[0].type == 'ELSE':
            node = p.command
        
        return node


    @_(
        'and_expression',
        'and_expression OR or_expression'
    )
    def or_expression(self, p):
        values = p._slice
        type = values[0].type

        node = NoOp()
        if type == 'and_expression' and len(values) == 1:
            node = p.and_expression

        elif type == 'and_expression' and len(values) > 1:
            token_type = TokenTypes.OR
            token = Token(token_type=token_type, value=values[1].value)
            node = BinOp(value=token, child1=p.and_expression, child2=p.or_expression)

        return node


    @_(
        'equal_expression',
        'equal_expression AND and_expression'
    )
    def and_expression(self, p):
        values = p._slice
        type = values[0].type

        node = NoOp()
        if type == 'equal_expression' and len(values) == 1:
            node = p.equal_expression

        elif type == 'equal_expression' and len(values) > 1:
            token_type = TokenTypes.AND

            token = Token(token_type=token_type, value=values[1].value)
            node = BinOp(value=token, child1=p.equal_expresison, child2=p.and_expression)

        return node

    @_(
        'relative_expression',
        'relative_expression EQUAL equal_expression',
        'relative_expression NOT_EQUAL equal_expression'
    )
    def equal_expression(self, p):
        values = p._slice
        type = values[0].type

        node = NoOp()
        if type == 'relative_expression' and len(values) == 1:
            return p.relative_expression

        elif type == 'relative_expression' and len(values) > 1:
            token_type = TokenTypes.EQUAL
            if values[1].type == 'NOT_EQUAL':
                token_type = TokenTypes.NOT_EQUAL
            token = Token(token_type=token_type, value=values[1].value)
            node = BinOp(value=token, child1=p.relative_expression, child2=p.equal_expression)

        return node

    @_(
        'expression',
        'expression GREATER relative_expression',
        'expression LESSER relative_expression',
        'expression GREATER_EQUAL relative_expression',
        'expression LESSER_EQUAL relative_expression'
    )
    def relative_expression(self, p):
        values = p._slice
        type = values[0].type

        node = NoOp()
        if type == 'expression' and len(values) == 1:
            node = p.expression
        
        elif type== 'expression' and len(values) > 1:
            token_type = TokenTypes.GREATER
            op_type = values[1].type
            if op_type == 'LESSER':
                token_type = TokenTypes.LESSER
            elif op_type == 'GREATER_EQUAL':
                token_type = TokenTypes.GREATER_EQUAL
            elif op_type == 'LESSER_EQUAL':
                token_type = TokenTypes.LESSER_EQUAL
            
            token = Token(token_type=token_type, value=values[1].value)
            node = BinOp(value=token, child1=p.expression, child2=p.relative_expression)

        return node

    @_(
        'term',
        'term PLUS expression',
        'term MINUS expression'
    )
    def expression(self, p):
        values = p._slice
        type = values[0].type
        
        node = NoOp()
        if type == 'term' and len(values) == 1:
            node = p.term
        
        elif type == 'term' and len(values) > 1:
            token_type = TokenTypes.PLUS
            if values[1].type == 'MINUS':
                token_type = TokenTypes.MINUS
            token = Token(token_type=token_type, value=values[1].value)
            node = BinOp(value=token, child1=p.term, child2=p.expression)

        return node

    @_(
        'factor',
        'factor MULTIPLICATION term',
        'factor DIVISION term'
    )
    def term(self, p):
        values = p._slice
        type = values[0].type
        
        node = NoOp()
        if type == 'factor' and len(values) == 1:
            node = p.factor
        
        elif type == 'factor' and len(values) > 1:
            token_type = TokenTypes.MULTIPLICATION
            if values[1].type == 'DIVISION':
                token_type = TokenTypes.DIVISION
            token = Token(token_type=token_type, value=values[1].value)
            node = BinOp(value=token, child1=p.factor, child2=p.term)

        return node

    @_(
        'NUMBER',
        'PLUS factor %prec UPLUS',
        'MINUS factor %prec UMINUS',
        'PARENTHESIS_OPEN or_expression PARENTHESIS_CLOSE',
        'IDENTIFIER PARENTHESIS_OPEN { or_expression } PARENTHESIS_CLOSE',
        'IDENTIFIER',
        'STRING',
        'TRUE',
        'FALSE'
    )
    def factor(self, p):
        values = p._slice
        type = values[0].type
        token_value = values[0].value
        
        node = NoOp()
        if type == 'NUMBER':
            token = Token(token_type=TokenTypes.INT, value=token_value)
            node = IntVal(value=token)
        
        elif type == 'PLUS':
            token = Token(token_type=TokenTypes.PLUS, value=token_value)
            node = UnOp(value=token, child=p.factor)
        
        elif type == 'MINUS':
            token = Token(token_type=TokenTypes.MINUS, value=token_value)
            node = UnOp(value=token, child=p.factor)
        
        elif type == 'PARENTHESIS_OPEN':
            return p.or_expression
        
        elif type == 'IDENTIFIER':
            if len(values) > 1:
                args = []
                for arg in p.or_expression:
                    args.append(arg)
                
                node = FuncCall(value=token_value, children=args)
            else:
                node = Variable(value=token_value)

        elif type == 'STRING':
            token = Token(token_type=TokenTypes.STRING, value=token_value)
            node = StringVal(value=token)

        elif type == 'TRUE':
            token = Token(token_type=TokenTypes.TRUE, value=True)
            node = BoolVal(value=token)
        
        elif type == 'FALSE':
            token = Token(token_type=TokenTypes.FALSE, value=False)
            node = BoolVal(value=token)

        return node

