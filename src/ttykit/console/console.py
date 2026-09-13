import sys
import os
from typing import Optional, Literal, Mapping
from ttykit.segmentation import Segmentation
from getpass import getpass

from .const import ColorSystem, WINDOWS

class Console:
    """
    Class for controling terminal events

    Args:
        color_system (str, Optional): Color system of the terminal. Either `standard`, `256` or `truecolor`. Leave as `auto` to autodetect.
        width (int): width of the terminal. If state is `None`, calculates it automatically.
        height (int): height of the terminal. If state is `None`, calculates it automatically.
        stderr (bool): use `stderr` for errors instead of stdout. Default `False`.
        no_color (bool): if `True`, the terminal be without colors, only monochrome (white and black). Default `False`.
        force_terminal (bool): if `True` use terminal control codes in any situation.
    """

    _environ: Mapping[str, str] = os.environ

    def __init__(self, 
        color_system: Optional[Literal["auto", "standard", "256", "truecolor", "windows"]] = "auto", 
        width: int = None, 
        height: int = None,
        stderr: bool = False,
        no_color: bool = False,
        force_terminal: Optional[bool] = False
    ):
        super().__init__()

        #? preparing to avoid any errors
        self._color_system = Optional[ColorSystem]
        self._force_terminal = None
        self.stderr = stderr
        self.no_color = no_color
        self.height = width
        self.width = height

        if color_system is None:
            self._color_system = None
        elif color_system == "auto":
            self._color_system =  self._detect_colorSystem()

        if force_terminal is not None:
            self._force_terminal = force_terminal

        if self.width is None:
            try:
                size = os.get_terminal_size()
                self.width = size.columns
            except OSError:
                print('Error calculating width of the terminal. Use default value (80)')
                self.width = 80

        if self.height is None:
            try:
                size = os.get_terminal_size()
                self.height = size.lines
            except OSError:
                print('Error calculating height of the terminal. Use default value (24)')
                self.height

    def _print_error(self, msg: str=None):
        if msg is None:
            return

        if self.stderr:
            sys.stderr.write(msg)

    @property
    def isTerminal(self) -> bool:
        """
        Check if the console writing to a terminal

        Returns:
            state (bool): return `True` if console is understanding escape sequences, otherwise `False`
        """
        if self._force_terminal is not None:
            return True

        if hasattr(sys.stdin, "__module__") and sys.stdin.__module__.startswith("idlelib"):
            return False #? return False for idle which claims to be a tty but can't handle ANSI codes

        ttyCompatyble = self._environ.get('TTY_COMPATIBLE', '')
        if ttyCompatyble == '0': #? 0 = device is not tty compatible
            return False
        elif ttyCompatyble =='1': #? 1 = device is tty compatible
            return True

        if not sys.stdout.isatty():
            return False


    @property
    def is_dumb_terminal(self) -> bool:
        """Detect dumb terminal.
    
        Returns:
            state (bool): `True` if writing to a dumb terminal, otherwise `False`.

        """
        is_dumb = self._environ.get("TERM", "").lower() in ("dumb", "unknown")
        return self.isTerminal and is_dumb


    @property
    def color_system(self):
        return self._detect_colorSystem()


    def _detect_colorSystem(self) -> Optional[ColorSystem]:
        """Autodetect the supported color theme fo the terminal"""

        if self.no_color:
            return None

        if WINDOWS:
            # TODO: add check for legacy windows
            
            if self._environ.get('COLORTERM') in ('truecolor', '24bit'):
                return ColorSystem.TRUECOLOR
            return ColorSystem.WINDOWS
        else:
            if self._environ.get('COLORTERM') in ('truecolor', '24bit'):
                return ColorSystem.TRUECOLOR
            
            if self._environ.get("TERM") in ("xterm-256color", "screen-256color"):
                return ColorSystem.EIGHT_BIT
            return ColorSystem.STANDARD

    def bell(self):
        sys.stdout.write("\a")
        sys.stdout.flush()

    def print(self,
            *args,
            sep: Optional[str] =" ",
            end: Optional[str] ="\n",
            justify: str = "left",
            fillchar: str = " "
            ) -> None:
        """
        Print the args to a stream

        Args:
            *args (Any): args to write to a stream
            sep (str | None): string inserted between values, default a space.
            end (str | None): string appended after the last value, default a newline.
            justify (str): justify of text in the terminal. Avaliable: "left", "center", "right".
            fillchar (str): char for fill free space in line. Default " ".
        Returns:
            None: write in `stdout`

        ### Example
            code:
                print("[blue] This is test string")

            output:
                <div style="color: blue;"> This is test string</div>
        """
        if not self.isTerminal or self.no_color:
            #? Just out, without colors or styles
            sys.stdout.write(sep.join(str(a) for a in args) + end)
            return

        #TODO: realize print logic with color style replace
        
        #? Apply the style with color to args
        text = sep.join(str(a) for a in args)

        text = Segmentation(text).auto_compile()

        match justify:
            case "left":
                text = text.ljust(self.width, fillchar)
            case "center":
                text = text.center(self.width, fillchar)
            case "right":
                text = text.rjust(self.width, fillchar)
            case unknown:
                raise ValueError(f"Unknown type '{unknown}' for text justify")
        
        sys.stdout.write(text + end)
        sys.stdout.flush()


    def input(self,
            prompt: str = '',
            *,
            password: bool = False,
            justify: str = "left",
            fillchar: str = " ") -> str:
        """
        Displays a prompt if have and waits for input from user.

        Args:
            prompt: text to render in prompt
            password (bool): if `True`, hide typed text. Default `False`
        Returns:
            result (str): typed text from user from stdin
        """

        if prompt:
            self.print(prompt, end='', justify=justify, fillchar=fillchar)

        if password:
            # TODO: realize text hidding
            result = getpass(prompt='')
        else:
            result = input()
        return result