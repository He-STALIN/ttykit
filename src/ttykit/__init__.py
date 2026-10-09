"""
        ttykit
=-=-=-=-=-=-=-=-=-=-=-
Helps produce attractive terminal output.

Author: He-STALIN
License: MIT License

Available imports:
    ├─ Classes:
    │     + Progress
    │     + Status
    │     + Tree
    │     + Console
    ├─ Submodules:
    │     + data
    │     - Input
    │     + utils
    ├─ Methods:
    │     + get_console
    └─ In dev/un-ready:
        - TUI (class)
        - Input (submodule)

Documentation you can see here:
    https://github.com/He-STALIN/ttykit/tree/main/docs
"""

from .console.console import Console
from .console import input as Input
from .progress import Progress
from .console.TUI import TUI
from .status import Status
from .tree import Tree
from . import data, utils


__all__ = [
    'Progress',
    'Status',
    'data',
    'Console',
    'Tree',
    'TUI',
    "Input",
    'get_console',
    'utils'
]

__name__ = 'ttykit'
__author__ = 'He-STALIN'
__version__ = '0.5.0b'
__license__ = 'MIT'


console_inst: "Console" = None

def get_console() -> 'Console':
    """Return a instance of `Console`"""
    global console_inst
    if console_inst:
        return console_inst
    else:
        console_inst = Console()
        return console_inst