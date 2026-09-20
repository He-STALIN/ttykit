from typing import List
from .console.console import Console

class Tree:
    """Build tree and render in terminal
    
    Args:
        label (str): name of current node.
    Returns:
        instance (self): instance of this class

    ### Methods
        add (label)
            adding child tree in main
        print ():
            render tree in terminal
    """
    def __init__(self, label: str):
        self.label = label
        self.children: List["Tree"] = []
        self.console = Console()

    def add(self, label: str) -> "Tree":
        """Adding child tree in current tree"""
        child = Tree(label)
        self.children.append(child)
        return child

    def _render(self, prefix: str = "", is_last: bool = True, is_root: bool = True) -> list:
        """Rendering tree nodes with lines

        Args:
            prefix (str): name of node
            is_last (bool): if `True`, use final line
            is_root (bool): if `True`, node have root access
        Returns:
            lines (list): list of tree lines
        """
        lines = []

        if is_root:
            lines.append(self.label)
            child_prefix = ""
        else:
            connector = "└── " if is_last else "├── "
            lines.append(prefix + connector + self.label)
            child_prefix = prefix + ("    " if is_last else "│   ")

        for i, child in enumerate(self.children):
            is_last_child = (i == len(self.children) - 1)
            lines.extend(child._render(child_prefix, is_last_child, is_root=False))

        return lines

    def print(self):
        """Render tree in terminal stream"""
        for line in self._render():
            self.console.print(line)