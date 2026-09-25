from ttykit.data.const import WINDOWS
from ttykit.data import KeyEvent
from typing import Callable
from ._local import str_to_KeyEvent, KeyEvent_to_str


if WINDOWS:
    from ._windows import WindowsKeyboard as _Keyboard
else:
    from ._unix import UnixKeyboard as _Keyboard
    Warning("Keyboard Event not fully completed")

_kb = _Keyboard()

# def get_vk_state(vk_code) -> bool:
#     """Return state of key
    
#     Args:
#         vk_code:
#             Virtual code of key.

#             Example: `0x10` (virtual code of SHIFT) -> state of shift key
#     Returns:
#         boolean state
#     """
#     return _kb.get_vk_state(vk_code)


def add_hotkey(hotkey: str | KeyEvent, callback: Callable) -> None:
    """Adds a hotkey that executes when pressed
    
    Args:
        hotkey (str | KeyEvent):
            Hotkey to which the call will be linked
        callback (callable):
            The method that will be called
    """
    _kb.add_hotkey(hotkey=hotkey, callback=callback)


def send(hotkey: str | KeyEvent) -> None:
    """Send hotkey press and release"""
    _kb.send(hotkey)


def release(hotkey: str | KeyEvent) -> None:
    """Release pressed key"""
    _kb.release(hotkey)


def press(hotkey: str | KeyEvent) -> None:
    """presses and holds the key"""
    _kb.press(hotkey)


def get_key() -> "KeyEvent":
    """Returns the pressed key"""
    return _kb.get_key()


def clear_all_hotkeys() -> None:
    """Reset all configured hotkeys"""
    _kb.clear_all_hotkey()


def clear_hotkey(hotkey: str | KeyEvent) -> None:
    """Reset configured hotkey"""
    _kb.clear_hotkey(hotkey)


__all__ = [
    get_vk_state,
    add_hotkey,
    send,
    release,
    press,
    get_key,
    clear_all_hotkeys,
    clear_hotkey,
    str_to_KeyEvent,
    KeyEvent_to_str
]