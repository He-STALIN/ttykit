from dataclasses import dataclass as _dataclass
from typing import Literal as _Literal


@_dataclass(frozen=True)
class KeyEvent:
    key: str
    key_code: int
    meta_key: bool = False
    alt_key: bool = False
    ctrl_key: bool = False
    shift_key: bool = False
    type: _Literal["key", "interrupt"] = "key"