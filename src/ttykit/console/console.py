import sys
import os
from typing import Optional, Literal, Mapping, Any
from ttykit import Colors, Styles

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
        self.height = None
        self.width = None

        if color_system is None:
            self._color_system = None
        elif color_system == "auto":
            self._color_system =  self._detect_colorSystem()

        if force_terminal is not None:
            self._force_terminal = force_terminal

        if width is None:
            try:
                size = os.get_terminal_size()
                width = size.columns
            except OSError:
                print('Error calculating width of the terminal. Use default value (80)')
                width = 80

        if height is None:
            try:
                size = os.get_terminal_size()
                height = size.lines
            except OSError:
                print('Error calculating height of the terminal. Use default value (24)')
                height

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

    def _get_style_code(self, style: str) -> str:
        styles = {
            'bold': Styles.BOLD,
            'dim': Styles.DIM,
            'italic': Styles.ITALIC,
            'underline': Styles.UNDERLINE,
            'blink': Styles.BLINK,
            'rapid_blink': Styles.RAPID_BLINK,
            'reverse': Styles.REVERSE
        }
        return styles.get(style, '')

    def _get_color_code(self, color: str) -> str:
        colors = {
            "black": Colors.BLACK,
            "red": Colors.RED,
            "green": Colors.GREEN,
            "yellow": Colors.YELLOW,
            "blue": Colors.BLUE,
            "purple": Colors.PURPLE,
            "cyan": Colors.CYAN,
            "white": Colors.WHITE,
            "dark_grey": Colors.DARK_GREY,
            "light_red": Colors.LIGHT_RED,
            "light_green": Colors.LIGHT_GREEN,
            "light_yellow": Colors.LIGHT_YELLOW,
            "light_blue": Colors.LIGHT_BLUE,
            "light_purple": Colors.LIGHT_PURPLE,
            "light_cyan": Colors.LIGHT_CYAN,
            "light_white": Colors.LIGHT_WHITE
        }
        return colors.get(color, "")

    def bell(self):
        sys.stdout.write("\a")
        sys.stdout.flush()

    def print(self,
            *args,
            sep: str | None=" ",
            end: str | None ="\n",
            style: str | None=None,
            color: str | None=None) -> None:
        """
        Print the args to a stream

        Args:
            *args (Any): args to write to a stream
            sep (str | None): string inserted between values, default a space.
            end (str | None): string appended after the last value, default a newline.
            style: style of args write to a steam, default `None`.
            color: color of args write to a stream, default `None`.
        Returns:
            None: write in `stdout`
        """
        if not self.isTerminal or self.no_color:
            #? Just out, without colors or styles
            sys.stdout.write(sep.join(str(a) for a in args) + end)
            return

        #TODO: realize print logic with color style replace
        
        #? Apply the style with color to args
        text = sep.join(str(a) for a in args)
        if color and self.color_system:
            color_code = self._get_color_code(color.lower())
            text = f"{color_code}{text}{Colors.RESET}"

        if style:
            style_code = self._get_style_code(style.lower())
            text = f"{style_code}{text}"

        sys.stdout.write(text + end)
        sys.stdout.flush()


    def input(self,
            prompt = '',
            *,
            style: str | None = None,
            color: str | None = None,
            password: bool = False) -> str:
        """
        Displays a prompt if have and waits for input from user.

        Args:
            prompt: text to render in prompt
            style (str | None): style for prompt render. Required prompt
            color (str | None): color for prompt render. Required prompt
            password (bool): if `True`, hide typed text. Default `False`
        Returns:
            result (str): typed text from user from stdin
        """

        if prompt:
            self.print(prompt, style=style, color=color, end='')

        if password:
            # TODO: realize text hidding
            Warning("This attribute in developing. Please, set 'password=False'")
        else:
            result = input()
        return result