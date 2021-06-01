import sys
from src.Types.TokenTypes import TokenTypes
from src.SymbolTable import SymbolTable
from src.Parser import ZParser
from src.Tokenizer import ZTokenizer 
from src.Codegen.CodeGen import CodeGen

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
    with open('test_tokens.out', 'w') as tmp:
        for token in tokens:
            tmp.write(str(token) + '\n')
    
    # Tokenize and parse language
    tokens = lexer.tokenize(file_content)
    root = parser.parse(tokens)
    
    # Set functions declarations to symbol table
    symbol_table = SymbolTable()
    root.Evaluate(symbol_table)

    # Evaluate main function
    main_func = symbol_table.get_function('main')
    main_func_node = main_func.get("value", None)
    if main_func_node is None:
        raise ValueError('main function was not defined')
    returned_data = main_func_node.statements.Evaluate(symbol_table)

    # Check main function returned data type
    if returned_data is None:
        raise ValueError('main function did not return an int')

    returned_type = returned_data[0]
    if returned_type != TokenTypes.INT:
        raise ValueError('main did not return an int')