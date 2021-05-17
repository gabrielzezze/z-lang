import sys
from src.Parser import Parser

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError("No input file")
    
    file_path = sys.argv[1]

    if file_path[-2:] != '.z':
        raise ValueError('Invalid file type')

    with open(file=file_path, mode='r') as file:
        lines = file.read().splitlines()
        if len(lines) <= 0:
            raise ValueError(f'{file_path} is empty')
        code = " ".join(lines)
        Parser.run(code=code)

