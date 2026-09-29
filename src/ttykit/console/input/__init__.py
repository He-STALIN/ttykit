from ttykit.data import KeyEvent as _KeyEvent
from typing import Callable as _Callable
from ._local import str_to_KeyEvent, KeyEvent_to_str
import platform as _platform


if _platform.system() == "Windows":
    from ._windows import WindowsKeyboard as _Keyboard
elif _platform.system() == "Linux":
    from ._unix import UnixKeyboard as _Keyboard
    print(Warning("Keyboard Event not fully completed"))
# elif _platform.system() == "Darwin":
else:
    raise OSError(f"Unsupported operating system: {_platform.system()}")

_kb = _Keyboard()

def add_hotkey(hotkey: str | _KeyEvent, callback: _Callable) -> None:
    """Adds a hotkey that executes when pressed
    
    Args:
        hotkey (str | KeyEvent):
            Hotkey to which the call will be linked
        callback (Callable):
            The method that will be called
    """
    _kb.add_hotkey(hotkey=hotkey, callback=callback)


def send(hotkey: str | _KeyEvent) -> None:
    """Send hotkey press and release"""
    _kb.send(hotkey)


def release(hotkey: str | _KeyEvent) -> None:
    """Release pressed key"""
    _kb.release(hotkey)


def press(hotkey: str | _KeyEvent) -> None:
    """presses and holds the key"""
    _kb.press(hotkey)


def get_key() -> "_KeyEvent":
    """Returns the pressed key"""
    return _kb.get_key()


def clear_all_hotkeys() -> None:
    """Reset all configured hotkeys"""
    _kb.clear_all_hotkey()


def clear_hotkey(hotkey: str | _KeyEvent) -> None:
    """Reset configured hotkey"""
    _kb.clear_hotkey(hotkey)


__all__ = [
    'add_hotkey,'
    'send',
    'release',
    'press',
    'get_key',
    'clear_all_hotkeys',
    'clear_hotkey',
    'str_to_KeyEvent',
    'KeyEvent_to_str'
]