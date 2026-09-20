import sys, tty, select, termios

from ttykit.data import KeyEvent


class UnixKeyboard:
    def __init__(self):
        pass

    def add_hotkey(self, hotkey: str, callback) -> None:
        """Adds a hotkey that executes when pressed
        
        Args:
            hotkey (str | KeyEvent):
                Hotkey to which the call will be linked.
            callback (callable):
                The method that will be called.
        """
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

    def clear_hotkey(self, hotkey: str | KeyEvent) -> None:
        pass

    def str_to_KeyEvent(self, hotkey: str) -> KeyEvent:
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
    
    def KeyEvent_to_str(self, hotkey: KeyEvent) -> str:
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