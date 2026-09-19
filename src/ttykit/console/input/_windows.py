# system imports
from ctypes import windll, byref, sizeof
from typing import NoReturn, Callable
from threading import Thread
from time import sleep
import msvcrt
import re
# local imports
from ttykit.data import KeyEvent, EXTENDED_SYM, VK_CODES
from ttykit.data.const import INPUT, KEYBDINPUT

_user32 = windll.user32

class WindowsKeyboard:
    def __init__(self, exit_on_interrupt: bool = True):
        super().__init__()
        self.exit_on_interrupt = exit_on_interrupt
        self.hotkeys: dict = {}
        self.now_key: str = ""
        self._running: bool = False
        self._thread: Thread | None = None

        self._start()

    def _start(self) -> None:
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
            raise Exception(e)

    def _stop(self) -> None:
        self._running = False

        if self._thread is not None:
            self._thread.join(timeout=1)
            self._thread = None

    def _event_loop(self) -> NoReturn:
        while self._running:
            try:
                if msvcrt.kbhit():
                    final: str = None
                    extended: bytes = None
                    key: bytes = msvcrt.getch()
                    modif: str = ""

                    if key in [None, ""]:
                        continue
                
                    if key in [b"\x00", b"\xe0"]:
                        extended = msvcrt.getch()
                        final = extended.decode(encoding="utf-8", errors="ignore")
                        final = final.replace(final, EXTENDED_SYM.get(final, ""))
                    else:
                        final = key.decode(encoding="utf-8", errors="ignore")
                        if self.get_vk_state(0x11):
                            modif += "ctrl + "
                            if final and ord(final) < 0x20:
                                final = chr(ord(final) + 0x40)  # 0x03 → 'C'

                        if self.get_vk_state(0x10):
                            modif += "shift + "

                        if self.get_vk_state(0x12):
                            modif += "alt + "

                        if self.get_vk_state(0x5B):
                            modif += "meta + "

                        if final == "\x1b":
                            final = "ESC"

                        if final == " ":
                            final = "space"

                        if final == "\r":
                            final = "enter"

                        final = modif + final.lower()

                    if final not in ["", None]:
                        self.now_key = final

                    self._run_hotkey()

                sleep(0.01)
            except KeyboardInterrupt:
                if self.exit_on_interrupt:
                    self._stop()
                else:
                    continue

    def _run_hotkey(self):
        if self.now_key in self.hotkeys.keys():
            callback = self.hotkeys.get(self.now_key)
            callback()

    def _send(self, HexCode, keyup=False):
        try:
            x = ""
            if keyup:
                x = INPUT(type=1, ki=KEYBDINPUT(wVk=HexCode, dwFlags=0x0002))
            else:
                x = INPUT(type=1, ki=KEYBDINPUT(wVk=HexCode))

            _user32.SendInput(1, byref(x), sizeof(x))
        except Exception as e:
            raise e

    def _split_hotkey(self, hotkey: str | KeyEvent) -> tuple[str, list[str]]:
        if type(hotkey) == KeyEvent:
            hotkey = self.KeyEvent_to_str(hotkey)

        hotkey = re.sub(r"\s+", "", hotkey)
        keys = hotkey.split("+")
        key = keys[-1]
        modificators = keys[:-1]
        return key, modificators

    def _key_to_vk(self, key: str) -> str:
        if len(key) == 1:
            return hex(ord(key))
        else:
            return VK_CODES.get(key, "")



    def get_vk_state(self, vk_code) -> bool:
        """Return State of key"""
        return (_user32.GetAsyncKeyState(vk_code) & 0x8000) != 0

    def add_hotkey(self, hotkey: str | KeyEvent, callback: Callable) -> None:
        """Adds a hotkey that executes when pressed
        
        Args:
            hotkey (str | KeyEvent):
                Hotkey to which the call will be linked.
            callback (callable):
                The method that will be called.
        """
        if type(hotkey) == KeyEvent: #? checking type of hotkey
            hotkey = self.KeyEvent_to_str(hotkey)
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
        if type(hotkey) == KeyEvent: #? just in case
            hotkey = self.KeyEvent_to_str(hotkey)
        elif type(hotkey) == str:
            hotkey = re.sub(r"\s+", "", hotkey)
        elif type(hotkey) not in [str, KeyEvent]:
            raise TypeError(f"Argument hotkey can be 'str' or 'KeyEvent'. Not be {type(hotkey)}")
        
        self.press(hotkey)
        sleep(0.02) #? wait 20ms for processing
        self.release(hotkey)

    def release(self, hotkey: str | KeyEvent) -> None:
        """Release the pressed hotkey"""
        if type(hotkey) == KeyEvent:
            hotkey = self.KeyEvent_to_str(hotkey)
        elif type(hotkey) == str:
            hotkey = re.sub(r"\s+", "", hotkey)
        elif type(hotkey) not in [str, KeyEvent]:
            raise TypeError(f"Argument hotkey can be 'str' or 'KeyEvent'. Not be {type(hotkey)}")

        try:
            main, modif = self._split_hotkey(hotkey)

            self._send(self._key_to_vk(main), keyup=True) # release main key

            for mod in reversed(modif): # release all modificators
                self._send(self._key_to_vk(mod), keyup=True)
        except Exception as e:
            raise e

    def press(self, hotkey: str | KeyEvent) -> None:
        """Presses and holds hotkey"""
        if type(hotkey) == KeyEvent:
            hotkey = self.KeyEvent_to_str(hotkey)
        elif type(hotkey) == str:
            hotkey = re.sub(r"\s+", "", hotkey)
        elif type(hotkey) not in [str, KeyEvent]:
            raise TypeError(f"Argument hotkey can be 'str' or 'KeyEvent'. Not be {type(hotkey)}")

        try:
            main, modif = self._split_hotkey(hotkey)

            for mod in modif:
                self._send(self._key_to_vk(mod), keyup=False)

            self._send(self._key_to_vk(main), keyup=False)

        except Exception as e:
            raise e

    def get_key(self) -> "KeyEvent":
        """Return the state of pressed key
        
        Returns:
            key_state (KeyEvent)
        """
        splited_key = self.now_key.split(" + ") #? split & clear from plus with spaces
        key = splited_key.pop()
        print(splited_key)
        return KeyEvent(
            key = key,
            key_code = ord(key),
            meta_key = True if "meta" in splited_key else False,
            alt_key= True if "alt" in splited_key else False,
            ctrl_key= True if "ctrl" in splited_key else False,
            shift_key= True if "shift" in splited_key else False,
            type = "key"
        )

    def clear_all_hotkey(self) -> None:
        """Reset all configured hotkeys"""
        self.hotkeys.clear()
        self.hotkeys = {} #? if "clear()" didn't work

    def clear_hotkey(self, hotkey: str | KeyEvent) -> None:
        """Reset configured hotkey"""
        keys = re.sub(r"\s+", "", hotkey)
        keys = keys.split("+")
        hotkey = " + ".join(keys)

        self.hotkeys.pop(hotkey)

    def str_to_KeyEvent(hotkey: str) -> KeyEvent:
        """Convert string representation to KeyEvent"""
        if type(hotkey) != str:
            raise TypeError(f"Argument 'hotkey' can be only 'str'. Not be {type(hotkey)}")

        hotkey = re.sub(r"\s+", "", hotkey)
        keys = hotkey.split("+")
        key = ""

        for iter in keys:
            if len(iter) == 1:
                key = iter
                break

        return KeyEvent(
            key= key,
            key_code= ord(key),
            meta_key= True if "meta" in keys else False,
            alt_key= True if "alt" in keys else False,
            ctrl_key= True if "ctrl" in keys else False,
            shift_key= True if "shift" in keys else False,
            type= "key"
        )

    def KeyEvent_to_str(hotkey: KeyEvent) -> str:
        """Convert KeyEvent representation to string"""
        if type(hotkey) != KeyEvent:
            raise TypeError(f"Argument 'hotkey' can be only 'Keyevent'. Not be {type(hotkey)}")

        return str(
            ("ctrl + " if hotkey.ctrl_key else "")
            + ("shift + " if hotkey.shift_key else "")
            + ("alt + " if hotkey.alt_key else "")
            + ("meta + " if hotkey.meta_key else "") 
            + hotkey.key
        )




if __name__ == '__main__':
    kb = WindowsKeyboard()

    def test_call():
        print("work")

    kb.add_hotkey("shift + g", test_call)

    while True:
        pass
