from threading import Thread
from typing import Literal
import time

from .data._state import STATUS_ANIMATION, TaskState, Colors
from .console.console import Console

class Status:
    """
    Create animated status of task in the terminal

    Args:
        message (str): some description for task. Can't be empty
        spinner: animation for task executing. Avaliable animations: `bar`, `ball` ... see all `python -m ttykit.spinner`
        color: color of name of task unit. Default: cyan
    Returns:
        None: show task in the terminal
    Examples:
    ### Realization:
    ```python
    from ttykit import Status, TaskState

    with Status("Unit Test 8", spinner="dots12") as status:
        # <task1>
        status.set_message("Unit Test 9")
        # <task2>
        status.set_state(TaskState.SUCCESS)
    ```
    ### out when task1
    ```
    ⠀⢙ Loading Unit Test 8
    ```
    ### out when task2
    ```
    ⢀⠀ Loading Unit Test 9
    ```
    ### out when finished
    ```
    [  OK  ] Loading Unit Test 9
    ```
    """
    def __init__(self, message: str,
                spinner: Literal["bar", "ball", "dots", "dots12", "bouncingBar", "points", "wave", "pulse", "moon", "clock", "snake", "line", "box", "arc"]="bar",
                color="CYAN"):
        self.message = message
        self.color = color
        self.spinner = spinner
        self.state = TaskState.RUNNING
        self.frames = STATUS_ANIMATION.get(self.spinner, STATUS_ANIMATION['bar'])
        self.running = False
        self.animation_thread = None
        self.paused = False
        self.console = Console()

    def __enter__(self):
        self.running = True
        self._animate()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.running = False
        time.sleep(0.1)
        state_color = '[green]' if self.state == TaskState.SUCCESS else '[red]' if self.state == TaskState.ERROR else '[yellow]'
        state_text = "  OK  " if self.state == TaskState.SUCCESS else " FAIL " if self.state == TaskState.ERROR else " WARN "
        self.console.print(f"\r[{state_color}{state_text}[/]] Loading {self._get_color()}{self.message}[/]")

    def _animate(self):
        def run():
            i = 0
            while self.running:
                if not self.paused:
                    frame = self.frames[i % len(self.frames)]
                    self.console.print(f"\r{frame}[/] Loading {self._get_color()}{self.message}[/]", end="")
                    i += 1
                time.sleep(0.08)
        self.animation_thread = Thread(target=run, daemon=True)
        self.animation_thread.start()

    def _get_color(self):
        return Colors.get(self.color, Colors.get('cyan'))


    def set_message(self, new_message: str):
        """
        Edit text of task when task running

        Args:
            new_message (str): new message of task status
        """
        self.message = new_message

    def set_state(self, state: TaskState):
        """
        Set state of task

        Args:
            state (TaskState): Avaliable states: SUCCESS, ERROR, WARNING
        """
        self.state = state

    def pause(self):
        """Pause animation"""
        self.paused = True

    def resume(self):
        """Resume animation"""
        self.paused = False