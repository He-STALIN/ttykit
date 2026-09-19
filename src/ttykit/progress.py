from .data._state import BARS
from typing import Literal
import time
from .console.console import Console

class Progress:
    """
    Creating Custom Loading Bar in the terminal

    Args:
        total (int): max value of bar. Default: 100
        prefix (str): some description of bar. Can be empty
        bar_length (int): how many characters in bar length. Default: 30
        bar_style: bar performance style. Default: `line`. Avaliable styles: `line`, `points`, `blocks`, `arrow`. 
        frames (bool): use bracket or not. Default: `False`
        show_ETA (bool): show ETA (Estimated Time of Arrival). Default: `True`
    Returns:
        None: write in the terminal
    Examples:
        ### realization:
        ```python
        from ttykit import CustomProgress

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
    def __init__(self, total: int=100, prefix: str=None, bar_length: int=30, bar_style: Literal["line", "points", "blocks", "arrow"]='line', frames: bool=False, show_ETA: bool = True):
        self.total = total
        self.prefix = prefix if prefix else ""
        self.bar_length = bar_length
        self.frames = frames
        temp = BARS.get(bar_style)
        self.bar_filled = temp['filled']
        self.bar_bg = temp['bg']
        self.current = 0
        self.finished = False
        self.show_ETA = show_ETA
        self.console = Console()

        if self.show_ETA:
            self.start_time = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.finished:
            self.finish()

    def update(self, value):
        if not self.finished:
            self.current = min(value, self.total)
            self._render()

    def advance(self, step: int=1):
        """
        increase state on some steps

        Args:
            step (int): count of step. Default: 1
        """
        self.update(self.current + step)

    def _render(self):
        percent =  int(self.current / self.total * 100)
        filled = int(self.current / self.total * self.bar_length)
        bar = str(self.bar_filled) * filled + str(self.bar_bg) * (self.bar_length - filled)

        eta: str = "ETA: --:--:--" if self.show_ETA else ""
        if self.show_ETA and self.current > 0:
            elapsed = time.time() - self.start_time
            rate = self.current / elapsed
            seconds = (self.total - self.current) / rate
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            eta = f"ETA: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
        
        self.console.print(f"\r{self.prefix} {"[ " if self.frames else ""}{bar}{" ]" if self.frames else ""} {percent}% {eta}")

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