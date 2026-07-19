import sys
from ._state import *

class CustomProgress:
    """
    Creating Custom Loading Bar in the terminal

    Args:
        total (float | int): max value of bar. Default: 100
        prefix (str): some description of bar. Can be empty
        bar_length (int): how many characters in bar length. Default: 30
    Returns:
        None: write in the terminal
    Examples:
        ### realization:
        ```python
        with CustomProgress(total=50, prefix="Loading", bar_length=100) as progress:
            while not progress.finished:
                # <some action>
                progress.advance(2)
                if progress.current >= 20:
                    progress.stop() # Force stopping bar & exit
        ```
        ### out:
        ```
        Loading ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40%
        ```
    """
    def __init__(self, total: float | int=100, prefix: str=None, bar_length: int=30):
        self.total = total
        self.prefix = prefix
        self.bar_length = bar_length
        self.current = 0
        self.finished = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.finished:
            self.finish()

    def update(self, value):
        if not self.finished:
            self.current = min(value, self.total)
            self._render()

    def advance(self, step: int | float=1):
        """
        increase state on some steps

        Args:
            step (int | float): count of step. Default: 1
        """
        self.update(self.current + step)

    def _render(self):
        percent = int(self.current / self.total * 100)
        filled = int(self.current / self.total * self.bar_length)
        bar = f"{MAGENTA}━{RESET}" * filled + f"{GREY}━{RESET}" * (self.bar_length - filled)
        sys.stdout.write(f"\r{self.prefix} {bar} {percent}%")
        sys.stdout.flush()

    def stop(self):
        """
        Force stopping bar and exiting
        """
        print()
        self.finished = True

    def finish(self):
        """
        Set 100% and exiting
        """
        self.update(self.total)
        print()
        self.finished = True