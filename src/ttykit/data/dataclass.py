from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class KeyEvent:
    key: str
    key_code: int
    meta_key: bool = False
    alt_key: bool = False
    ctrl_key: bool = False
    shift_key: bool = False
    type: Literal["key", "interrupt"] = "key"