import sys, tty, select, termios, os
from threading import Thread
from typing import Callable
from time import sleep
import re

from ttykit.data import KeyEvent
from ._local import KeyEvent_to_str, str_to_KeyEvent


# Карта escape-последовательностей → понятные имена
LINUX_KEY_MAP = {
    # Стрелки
    '\x1b[A': 'UP',
    '\x1b[B': 'DOWN',
    '\x1b[C': 'RIGHT',
    '\x1b[D': 'LEFT',
    # F1–F4 (SS3-последовательности)
    '\x1bOP': 'F1',
    '\x1bOQ': 'F2',
    '\x1bOR': 'F3',
    '\x1bOS': 'F4',
    # F5–F12 (CSI-последовательности)
    '\x1b[15~': 'F5',
    '\x1b[17~': 'F6',
    '\x1b[18~': 'F7',
    '\x1b[19~': 'F8',
    '\x1b[20~': 'F9',
    '\x1b[21~': 'F10',
    '\x1b[23~': 'F11',
    '\x1b[24~': 'F12',
    # Прочие спецклавиши
    '\x1b[H': 'HOME',
    '\x1b[F': 'END',
    '\x1b[2~': 'INSERT',
    '\x1b[3~': 'DELETE',
    '\x1b[5~': 'PAGEUP',
    '\x1b[6~': 'PAGEDOWN',
    # Простые символы
    '\x1b': 'ESC',
    '\t': 'TAB'
}

class UnixKeyboard:
    def __init__(self):
        super().__init__()
        self.fd = sys.stdin.fileno()
        self.old_term = termios.tcgetattr(self.fd)
        self.hotkeys: dict = {}
        self.now_key: str = ""
        self._running: bool = False
        self._thread: Thread = None

        self._start()

    def _start(self):
        try:
            if self._running:
                return

            self._running = True
            self._thread = Thread(
                target=self._event_loop,
                daemon=True
            )

            self._thread.start()
        except Exception as e:
            raise e

    def _stop(self):
        self._running = False

        if self._thread is not None:
            self._thread.join(timeout=1)
            self._thread = None

    def _event_loop(self):
        while self._running:
            try:
                tty.setcbreak(self.fd)

                if select.select([sys.stdin], [], [], 0.1)[0]:
                    key = os.read(self.fd, 1) #sys.stdin.read(1)

                    if key in [None, ""]:
                        continue

                    if key in ["\x1b", "\t"]:
                        if key == "\x1b":
                            if select.select([sys.stdin], [], [], 0.1):
                                key += os.read(self.fd, 1)

                                if select.select([sys.stdin], [], [], 0.1):
                                    key += os.read(self.fd, 1) #sys.stdin.read(1)

                                    if select.select([sys.stdin], [], [], 0.1):
                                        key += os.read(self.fd, 1) #sys.stdin.read(1)
                        else:
                            self.now_key = LINUX_KEY_MAP.get(key, key)
                            self.now_key = key

                    print(fr"{list(self.now_key)}")

                    self._run_hotkey()
            except Exception as e:
                raise e
            finally:
                termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_term)
                sleep(0.01)


    def _run_hotkey(self):
        if self.now_key in self.hotkeys.keys():
            callback: Callable[[]] = self.hotkeys.get(self.now_key)
            callback()



    def add_hotkey(self, hotkey: str | KeyEvent, callback: Callable) -> None:
        """Adds a hotkey that executes when pressed
        
        Args:
            hotkey (str | KeyEvent):
                Hotkey to which the call will be linked.
            callback (callable):
                The method that will be called.
        """
        if type(hotkey) == KeyEvent: # ? checking type of hotkey
            hotkey = KeyEvent_to_str(hotkey)
        elif type(hotkey) == str:
            keys = re.sub(r"\s+", "", hotkey) # clear all spaces
            keys = keys.split("+")
            hotkey =  " + ".join(keys)
        elif type(hotkey) not in [str, KeyEvent]:
            raise TypeError(f"Argument 'hotkey' can be only 'str' or 'KeyEvent'. Not be {type(hotkey)}")
        
        
        if not callable(callback): #? checking callback type
            raise TypeError("Argument 'callback' must be callable")
        
        self.hotkeys[hotkey] = callback

    def send(self, hotkey: str | KeyEvent) -> None:
        """Presses hotkey and releases"""
        pass

    def release(self, hotkey: str | KeyEvent) -> None:
        """Release the pressed hotkey"""
        pass

    def press(self, hotkey: str | KeyEvent) -> None:
        """Presses and holds hotkey"""
        pass

    def get_key(self) -> "KeyEvent":
        """Return the state of pressed key
        
        Returns:
            key_state (KeyEvent)
        """
        pass

    def clear_all_hotkey(self) -> None:
        """Reset all configured hotkeys"""
        self.hotkeys.clear()
        self.hotkeys = {}

    def clear_hotkey(self, hotkey: str | KeyEvent) -> None:
        """Reset configured hotkey"""
        if type(hotkey) == KeyEvent:
            hotkey = KeyEvent_to_str(hotkey)
        elif type(hotkey) not in [str, KeyEvent]:
            raise TypeError(f"Argument 'hotkey' can be only 'str' or 'KeyEvent'. Not be {type(hotkey)}")
        
        keys = re.sub(r"\s+", "", hotkey)
        keys = keys.split("+")
        hotkey = " + ".join(keys)
        
        self.hotkeys.pop(hotkey)




if __name__ == "__main__":
    kb = UnixKeyboard()
    kb.add_hotkey("ctrl + c", lambda: print("Ctrl + C pressed"))
    kb.add_hotkey("ctrl + d", lambda: print("Ctrl + D pressed"))
    kb.add_hotkey("ctrl + e", lambda: print("Ctrl + E pressed"))
    kb.add_hotkey("ctrl + f", lambda: print("Ctrl + F pressed"))
    kb.add_hotkey("ctrl + g", lambda: print("Ctrl + G pressed"))
    kb.add_hotkey("ctrl + h", lambda: print("Ctrl + H pressed"))
    kb.add_hotkey("ctrl + i", lambda: print("Ctrl + I pressed"))
    kb.add_hotkey("ctrl + j", lambda: print("Ctrl + J pressed"))
    kb.add_hotkey("ctrl + k", lambda: print("Ctrl + K pressed"))
    kb.add_hotkey("ctrl + l", lambda: print("Ctrl + L pressed"))
    kb.add_hotkey("ctrl + m", lambda: print("Ctrl + M pressed"))
    kb.add_hotkey("ctrl + n", lambda: print("Ctrl + N pressed"))
    kb.add_hotkey("ctrl + o", lambda: print("Ctrl + O pressed"))
    kb.add_hotkey("ctrl + p", lambda: print("Ctrl + P pressed"))
    kb.add_hotkey("ctrl + q", lambda: print("Ctrl + Q pressed"))
    kb.add_hotkey("ctrl + r", lambda: print("Ctrl + R pressed"))
    kb.add_hotkey("ctrl + s", lambda: print("Ctrl + S pressed"))
    kb.add_hotkey("ctrl + t", lambda: print("Ctrl + T pressed"))
    kb.add_hotkey("ctrl + u", lambda: print("Ctrl + U pressed"))
    kb.add_hotkey("ctrl + v", lambda: print("Ctrl + V pressed"))
    kb.add_hotkey("ctrl + w", lambda: print("Ctrl + W pressed"))
    kb.add_hotkey("ctrl + x", lambda: print("Ctrl + X pressed"))
    kb.add_hotkey("ctrl + y", lambda: print("Ctrl + Y pressed"))

    while True:
        pass