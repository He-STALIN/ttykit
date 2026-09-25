from ttykit.data import KeyEvent
import re

def str_to_KeyEvent(hotkey: str) -> "KeyEvent":
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