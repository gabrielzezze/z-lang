from src.SymbolTable import SymbolTable
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

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbol_table: SymbolTable):
        pass

    def traverse(self, n, level=0):
        if n == None:
            return ""

        tabs: str = "\t" * int(level) if int(level) > 0 else ""

        node_type = type(n)
        out_str = ''

        if node_type == BinOp:
            out_str = f'BinOp - {n.value.type}'
        elif node_type == UnOp:
            out_str = f'UnOp - {n.value.type}'
        elif node_type == NoOp:
            out_str = f'NoOp'
        elif node_type == IntVal:
            out_str = f'IntVal - {n.value.value}'
        elif node_type == BoolVal:
            out_str = f'BoolVal - {n.value.value}'
        elif node_type == StringVal:
            out_str = f'StringVal - {n.value.value}'
        elif node_type == Variable:
            out_str = f'Variable - {n.value}'
        elif node_type == Identifier:
            out_str = f'Identifier - {n.value}'
        elif node_type == Print:
            out_str = f'Print'
        elif node_type == Block:
            out_str = f'Block'
        elif node_type == IfElseOp:
            out_str = f'IfElse'
        elif node_type == WhileOp:
            out_str = f'While'
            
        return out_str


    def __str__(self) -> str:
        return self.traverse(self, 0)
    