from os import name
from src.Types.TokenTypes import TokenTypes
from src.Node import Node
from src.SymbolTable import SymbolTable
from src.Nodes.FuncArguments import FuncArguments
from llvmlite import ir

class FuncDeclaration(Node):
    def __init__(self, func_name, statements, args: FuncArguments):
        self.args = args
        self.statements = statements
        super().__init__(
            value=func_name, 
            children=[statements, args],
            node_type='FUNCDEC'
        )

    def Evaluate(self, symbol_table: SymbolTable):
        if self.value == 'main':
            symbol_table.set_function('main', self, symbol_table, None)
            return
        func_return_type = None
        if self.args.args[self.value]['type'].type == TokenTypes.INT:
            func_return_type = ir.IntType(8)
        elif self.args.args[self.value]['type'].type == TokenTypes.BOOL_TYPE:
            func_return_type = ir.IntType(1)
        else:
            func_return_type = ir.ArrayType(ir.IntType(8), 64)

        
        args_types = []
        defined_args = self.args.args
        for arg in self.args.args.keys():
            if arg == self.value:
                continue

            if defined_args[arg]['type'] == TokenTypes.INT:
                args_types.append(ir.IntType(8))
            elif defined_args[arg]['type']  == TokenTypes.BOOL_TYPE:
                args_types.append(ir.IntType(1))
            else:
                args_types.append(ir.ArrayType(ir.IntType(8), 64))

        func_type = ir.FunctionType(func_return_type, args_types)
        func_i = ir.Function(self.module, func_type, name=self.value)

        func_entry_block = func_i.append_basic_block(f'func_{self.value}_entry')

        previous_position = self.builder
        Node.builder = ir.IRBuilder(func_entry_block)

        args_pointers = []
        func_symbol_table = SymbolTable()
        func_symbol_table.functions = symbol_table.functions
        args_keys = list(self.args.args.keys())
        for idx, arg in enumerate(args_types):
            arg_pointer = self.builder.alloca(arg, name=f'{args_keys[idx+1]}')
            self.builder.store(func_i.args[idx], arg_pointer)
            args_pointers.append(arg_pointer)
        
        for idx, ptr in enumerate(args_pointers):
            func_symbol_table.set(f'{args_keys[idx+1]}', ptr)

        symbol_table.set_function(key=self.value, value=self, func_symbol_table=func_symbol_table, func_i=func_i)
        self.statements.Evaluate(func_symbol_table)
        Node.builder = previous_position
        return
