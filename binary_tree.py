from ast import arg
from tree_node import *

class Tree:
    def __init__(self, *args) -> None:
        if len(args) < 1:
            self.root = None
        elif isinstance(args[0], int):
            self.root = TreeNode(args[0])