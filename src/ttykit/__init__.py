"""Helping made beatiful out in terminal"""
import traceback
import sys

from .data import TaskState, Colors, Styles, RESET
from .console.console import Console
from .console import input as Input
from .progress import Progress
from .console.TUI import TUI
from .status import Status
from .tree import Tree

__colors__ = [
    Colors,
    Styles,
    RESET
]

__all__ = [
    'Progress',
    'Status',
    'TaskState',
    'Console',
    'Tree',
    'TUI',
    'get_console',
    'set_custom_hook',
    "Input",
    __colors__
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

def custom_excepthook(exc_type, exc_value, exc_tb):
    tb_lines = traceback.format_exception(exc_type, exc_value, exc_tb)
    
    # Самая длинная строка
    error_line = f"Error: {exc_type.__name__}"
    msg_line = f"Message: {exc_value}"
    max_len = max(len(error_line), len(msg_line), 40)
    
    # Рамка
    print(f"╔{'═' * (max_len + 4)}╗")
    print(f"║  {Colors.RED}{error_line.ljust(max_len)}{RESET}  ║")
    print(f"║  {Colors.RED}{msg_line.ljust(max_len)}{RESET}  ║")
    print(f"╠{'═' * (max_len + 4)}╣")
    
    for line in tb_lines[-3:]:
        clean = line.strip()
        if len(clean) > max_len:
            clean = clean[:max_len-3] + "..."
        print(f"║  {clean.ljust(max_len)}  ║")
    
    print(f"╚{'═' * (max_len + 4)}╝")

def set_custom_hook(Traceback: bool=False) -> None:
    """
    Set a custom methods

    Args:
        Traceback (bool): replace Traceback on custom or not. Default `False`
    """

    print("[WARNING] this method 'set_custom_hook' unstable and may not working")

    if Traceback:
        print('set custom excepthook...')
        sys.excepthook = custom_excepthook