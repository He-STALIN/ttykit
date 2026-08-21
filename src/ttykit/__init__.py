"""Helping made beatiful out in terminal"""

from .progress import Progress
from .status import Status
from ._state import TaskState, Colors, Styles, RESET
from .console.console import Console
from .console.TUI import TUI
import traceback
import sys

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
    'TUI',
    'get_console',
    'set_custom_hook'
]

def get_console() -> 'Console':
    """Return a instance of `Console`"""
    console = Console()
    return console

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

def set_custom_hook(Traceback: bool= False) -> None:
    """
    Set a custom methods

    Args:
        Traceback (bool): replace Traceback on custom or not. Default `False`
    """

    if Traceback:
        print('set custom excepthook...')
        sys.excepthook = custom_excepthook

__name__ = 'ttykit'
__author__ = 'He-STALIN'
__version__ = '0.3.7'
__license__ = 'MIT'