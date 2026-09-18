from enum import IntEnum
import sys

WINDOWS = sys.platform == "win32"

class ColorSystem(IntEnum):
    """One of the 3 color system supported by terminals."""

    STANDARD = 1
    EIGHT_BIT = 2
    TRUECOLOR = 3
    WINDOWS = 4

    def __repr__(self) -> str:
        return f"ColorSystem.{self.name}"

    def __str__(self) -> str:
        return repr(self)


EXTENDED_SYM = {
    "H": "UpArrow",
    "P": "DownArrow",
    "K": "LeftArrow",
    "M": "RightArrow",
    "R": "Insert",
    "G": "Home",
    "I": "PageUp",
    "Q": "PageDown",
    "S": "Delete",
    "O": "End",
    #? Function keys
    ";": "F1",
    "<": "F2",
    "=": "F3",
    ">": "F4",
    "?": "F5",
    "@": "F6",
    "A": "F7",
    "B": "F8",
    "C": "F9",
    "D": "F10",
    "": "F11",
    "": "F12",
}