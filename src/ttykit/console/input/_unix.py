import sys, tty, select, termios

from ttykit.data.dataclass import KeyEvent


class UnixKeyboard:
    def __init__(self):
        pass

    def add_hotkey(self, hotkey: str, callback) -> None:
        pass

    def send(self, hotkey: str) -> None:
        pass

    def release(self, hotkey: str) -> None:
        pass

    def press(self, hotkey: str) -> None:
        pass

    def get_key(self) -> "KeyEvent":
        pass

    def clear_all_hotkey(self) -> None:
        pass