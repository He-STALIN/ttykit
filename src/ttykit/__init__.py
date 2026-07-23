"""Helping made beatiful out in terminal"""

from .progress import Progress
from .status import Status
from ._state import TaskState, Colors, Styles, RESET

__colors__ = [
    Colors,
    Styles,
    RESET
]

__all__ = [
    'Progress',
    'Status',
    'TaskState'
]

__name__ = 'ttykit'
__author__ = 'He-STALIN'
__version__ = '0.2.2'
__license__ = 'MIT'