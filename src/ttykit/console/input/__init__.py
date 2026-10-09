from typing import Callable as _Callable
import platform as _platform
from warnings import warn

from ._local import str_to_KeyEvent, KeyEvent_to_str
from ttykit.utils import InputWarning, SupportError
from ttykit.data import KeyEvent as _KeyEvent

if _platform.system() == "Windows":
    from ._windows import WindowsKeyboard as _Keyboard
elif _platform.system() == "Linux":
    from ._unix import UnixKeyboard as _Keyboard
    warn(
        "Unix-related keyboard reader not fully made and may contain critical bugs",
        InputWarning,
        stacklevel=2
    )
# elif _platform.system() == "Darwin":
else:
    raise SupportError(f"Unsupported operating system: {_platform.system()}")

_kb = None

def add_hotkey(hotkey: str | _KeyEvent, callback: _Callable) -> None:
    """Adds a hotkey that executes when pressed
    
    Args:
        hotkey (str | KeyEvent):
            Hotkey to which the call will be linked
        callback (Callable):
            The method that will be called
    """
    _get_kb().add_hotkey(hotkey=hotkey, callback=callback)


def send(hotkey: str | _KeyEvent) -> None:
    """Send hotkey press and release"""
    _get_kb().send(hotkey)


def release(hotkey: str | _KeyEvent) -> None:
    """Release pressed key"""
    _get_kb().release(hotkey)


def press(hotkey: str | _KeyEvent) -> None:
    """presses and holds the key"""
    _get_kb().press(hotkey)


def get_key() -> "_KeyEvent":
    """Returns the pressed key"""
    return _get_kb().get_key()


def clear_all_hotkeys() -> None:
    """Reset all configured hotkeys"""
    _get_kb().clear_all_hotkeys()


def clear_hotkey(hotkey: str | _KeyEvent) -> None:
    """Reset configured hotkey"""
    _get_kb().clear_hotkey(hotkey)


def _get_kb():
    global _kb
    if _kb is None:
        _kb = _Keyboard()
        return _kb
    else:
        return _kb

__all__ = [
    'add_hotkey',
    'send',
    'release',
    'press',
    'get_key',
    'clear_all_hotkeys',
    'clear_hotkey',
    'str_to_KeyEvent',
    'KeyEvent_to_str'
]