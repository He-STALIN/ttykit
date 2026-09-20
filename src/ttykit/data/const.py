from enum import IntEnum
import ctypes
from ctypes.wintypes import WORD, DWORD, ULONG
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


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", WORD), # virt key code
        ("wScan", WORD), # scan code
        ("dwFlags", DWORD), # flags
        ("time", DWORD), # time of event
        ("dwExtraInfo", ULONG) # additional info
    ]

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [
            ("ki", KEYBDINPUT)
            ]

    _anonymous_ = ("_input",)  # чтобы обращаться к ki напрямую
    _fields_ = [
        ("type", DWORD),
        ("_input", _INPUT),
    ]

EXTENDED_SYM: dict[str, str] = {
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

class VK_CODES:
    #? Mouse Buttons
    MOUSE_LBUTTON = 0x01
    MOUSE_RBUTTON = 0x02
    MOUSE_MBUTTON = 0x04
    MOUSE_X1BUTTON = 0x05
    MOUSE_X2BUTTON = 0x06
    #? Keyboard Buttons
    SHIFT = 0x10
    CTRL = 0x11
    ALT = 0x12
    PAUSE = 0x13
    CAPSLOCK = 0x14
    LESSTHAN = 0x3C
    LWIN = 0x5B
    RWIN = 0x5C
    BACKSPACE = 0x08
    TAB = 0x09
    ENTER = 0x0D
    EQUALS = 0x3D
    PLUS = 0x2B
    MINUS = 0x2D
    PERIOD = 0x2E
    SLASH = 0x2F
    BACKSLASH = 0x2C
    #? NUMPAD
    NUM0 = 0x60
    NUM1 = 0x61
    NUM2 = 0x62
    NUM3 = 0x63
    NUM4 = 0x64
    NUM5 = 0x65
    NUM6 = 0x66
    NUM7 = 0x67
    NUM8 = 0x68
    NUM9 = 0x69
    NUM_MULTIPLY = 0x6A


    def get(name: str, default: str | None = None):
        """Return the value for key if key is in the class else default"""

        match name.lower():
            case "lmb":
                return VK_CODES.MOUSE_LBUTTON
            case "mmb":
                return VK_CODES.MOUSE_MBUTTON
            case "rmb":
                return VK_CODES.MOUSE_RBUTTON
            case "x1mb":
                return VK_CODES.MOUSE_X1BUTTON
            case "x2mb":
                return VK_CODES.MOUSE_X2BUTTON
            case "shift":
                return VK_CODES.SHIFT
            case "ctrl":
                return VK_CODES.CTRL
            case "alt":
                return VK_CODES.ALT
            case "pause":
                return VK_CODES.PAUSE
            case "capslock":
                return VK_CODES.CAPSLOCK
            case "lessthan":
                return VK_CODES.LESSTHAN
            case "lwin":
                return VK_CODES.LWIN
            case "rwin":
                return VK_CODES.RWIN
            case "backspace":
                return VK_CODES.BACKSPACE
            case "tab":
                return VK_CODES.TAB
            case "enter":
                return VK_CODES.ENTER
            case "equals":
                return VK_CODES.EQUALS
            case "plus":
                return VK_CODES.PLUS
            case "minus":
                return VK_CODES.MINUS
            case "period": 
                return VK_CODES.PERIOD
            case "slash": 
                return VK_CODES.SLASH
            case "backslash": 
                return VK_CODES.BACKSLASH
            case "num0":
                return VK_CODES.NUM0
            case "num1":
                return VK_CODES.NUM1
            case "num2":
                return VK_CODES.NUM2
            case "num3":
                return VK_CODES.NUM3
            case "num4":
                return VK_CODES.NUM4
            case "num5":
                return VK_CODES.NUM5
            case "num6":
                return VK_CODES.NUM6
            case "num7":
                return VK_CODES.NUM7
            case "num8":
                return VK_CODES.NUM8
            case "num9":
                return VK_CODES.NUM9
            case "num_multiply":
                return VK_CODES.NUM_MULTIPLY