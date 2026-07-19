"""Helping made beatiful out in terminal"""

from .progress import CustomProgress
from .status import CustomStatus
from ._state import TaskState, Colors, Styles, RESET

__colors__ = [
    Colors,
    Styles,
    RESET
]

__all__ = [
    'CustomProgress',
    'CustomStatus',
    'TaskState'
]

__name__ = 'ttykit'
__author__ = 'He-STALIN'
__version__ = '0.1.5'
__license__ = 'MIT'