import sys
from src.Node import Node
from src.Types.TokenTypes import TokenTypes
from src.SymbolTable import SymbolTable
from src.Parser import ZParser
from src.Tokenizer import ZTokenizer 
from src.Codegen.CodeGen import CodeGen
from llvmlite import ir


if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        raise ValueError("No input file")
    
    # Get file path and read content
    file_path = sys.argv[1]
    if file_path[-2:] != '.z':
        raise ValueError('Invalid file type')
    with open(file=file_path, mode='r') as file:
        file_content = file.read()

    # Instantiate lexer and parse
    lexer = ZTokenizer()
    parser = ZParser()
    codegen = CodeGen()


    # Get tokens from file
    tokens = lexer.tokenize(file_content)
    with open('debug/test_tokens.out', 'w') as tmp:
        for token in tokens:
            tmp.write(str(token) + '\n')
    
    # Tokenize and parse language
    tokens = lexer.tokenize(file_content)
    root = parser.parse(tokens)
    
    # Codegen vars
    module = codegen.module
    builder = codegen.builder
    printf = codegen.printf

    Node.module = module
    Node.builder = builder
    Node.printf = printf

    fmt = "%i \n\0"
    c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))
    Node.global_fmt = ir.GlobalVariable(module, c_fmt.type, name="fstr")
    Node.global_fmt.linkage = 'internal'
    Node.global_fmt.global_constant = True
    Node.global_fmt.initializer = c_fmt

    # Set functions declarations to symbol table
    symbol_table = SymbolTable()
    root.Evaluate(symbol_table)

    # Evaluate main function
    main_func = symbol_table.get_function('main')
    main_func_node = main_func.get("value", None)
    if main_func_node is None:
        raise ValueError('main function was not defined')

    symbol_table.functions['main']['pointer'] = codegen.base_func
    # print(main_func_node)
    # print(main_func_node.statements.children)
    main_func_node.statements.Evaluate(symbol_table)
    
    codegen.create_ir()
    codegen.save_ir('out/output.ll')