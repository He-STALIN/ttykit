"""Helping made beatiful out in terminal"""

from .progress import CustomProgress
from .status import CustomStatus
from ._state import TaskState, CYAN, MAGENTA, DARK_GREY, GREEN, GREY, RED, RESET, YELLOW

__colors__ = [
    CYAN,
    MAGENTA,
    DARK_GREY,
    GREEN,
    GREY,
    RED,
    YELLOW,
    RESET
]

__all__ = [
    'CustomProgress',
    'CustomStatus',
    TaskState
]

__name__ = 'ttykit'
__author__ = 'He-STALIN'
__version__ = '0.1.3'
__license__ = 'MIT'