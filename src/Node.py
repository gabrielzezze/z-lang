from src.SymbolTable import SymbolTable
import uuid

class Node:
    builder = None
    printf = None
    module = None
    global_fmt = None

    def __init__(self, value, children, node_type):
        self.value = value
        self.children = children
        self.node_type = node_type
        self.id = str(uuid.uuid4()).replace('-', '_')

    def Evaluate(self, symbol_table: SymbolTable):
        pass

    def traverse(self, n, level=0):
        if n == None:
            return ""

        tabs: str = "\t" * int(level) if int(level) > 0 else ""

        node_type = n.node_type
        out_str = ''

        if node_type == 'BinOp':
            out_str = f'BinOp - {n.value.type}'
        elif node_type == 'UnOp':
            out_str = f'UnOp - {n.value.type}'
        elif node_type == 'NoOp':
            out_str = f'NoOp'
        elif node_type == 'IntVal':
            out_str = f'IntVal - {n.value.value}'
        elif node_type == 'BoolVal':
            out_str = f'BoolVal - {n.value.value}'
        elif node_type == 'StringVal':
            out_str = f'StringVal - {n.value.value}'
        elif node_type == 'Variable':
            out_str = f'Variable - {n.value}'
        elif node_type == 'Identifier':
            out_str = f'Identifier - {n.value}'
        elif node_type == 'Print':
            out_str = f'Print'
        elif node_type == 'Block':
            out_str = f'Block'
        elif node_type == 'IfElseOp':
            out_str = f'IfElse'
        elif node_type == 'WhileOp':
            out_str = f'While'
        elif node_type == 'FuncOp':
            out_str = f'FuncOp'

        return out_str


    def __str__(self) -> str:
        return self.traverse(self, 0)
    