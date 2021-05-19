import sys
from src.SymbolTable import SymbolTable
from src.Parser import ZParser
from src.Tokenizer import ZTokenizer 

if __name__ == '__main__':
        # f = sys.argv[1]
        # with open(f, "r") as tmp:
        #     sentence = tmp.read()

    if len(sys.argv) < 2:
        raise ValueError("No input file")
    
    file_path = sys.argv[1]

    if file_path[-2:] != '.z':
        raise ValueError('Invalid file type')

    with open(file=file_path, mode='r') as file:
        file_content = file.read()

    lexer = ZTokenizer()
    parser = ZParser()

    tokens = lexer.tokenize(file_content)
    with open('test_tokens.out', 'w') as tmp:
        for token in tokens:
            tmp.write(str(token) + '\n')
    
    tokens = lexer.tokenize(file_content)
        
    root = parser.parse(tokens)
    
    symbol_table = SymbolTable()
    root.Evaluate(symbol_table)







# if __name__ == '__main__':
#     if len(sys.argv) < 2:
#         raise ValueError("No input file")
    
#     file_path = sys.argv[1]

#     if file_path[-2:] != '.z':
#         raise ValueError('Invalid file type')

#     with open(file=file_path, mode='r') as file:
#         lines = file.read().splitlines()
#         if len(lines) <= 0:
#             raise ValueError(f'{file_path} is empty')
#         code = " ".join(lines)
#         Parser.run(code=code)

