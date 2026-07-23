from threading import Thread
import time
import sys
from ._state import *

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
    from ttykit import CustomStatus, TaskState

    with CustomStatus("Unit Test 8", spinner="dots12") as status:
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
    def __init__(self, message: str, spinner="bar", color="CYAN"):
        self.message = message
        self.color = color
        self.spinner = spinner
        self.state = TaskState.RUNNING
        self.frames = STATUS_ANIMATION.get(self.spinner, STATUS_ANIMATION['bar'])
        self.running = False
        self.animation_thread = None
        self.paused = False

    def __enter__(self):
        self.running = True
        self._animate()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.running = False
        time.sleep(0.1)
        state_color = Colors.GREEN if self.state == TaskState.SUCCESS else Colors.RED if self.state == TaskState.ERROR else Colors.YELLOW
        state_text = "  OK  " if self.state == TaskState.SUCCESS else " FAIL " if self.state == TaskState.ERROR else " WARN "
        print(f"\r[{state_color}{state_text}{RESET}] Loading {self._get_color()}{self.message}{RESET}")

    def _animate(self):
        def run():
            i = 0
            while self.running:
                if not self.paused:
                    frame = self.frames[i % len(self.frames)]
                    print(f"\r{frame} Loading {self._get_color()}{self.message}{RESET}", end="")
                    sys.stdout.flush()
                    i += 1
                time.sleep(0.08)
        self.animation_thread = Thread(target=run, daemon=True)
        self.animation_thread.start()

    def _get_color(self):
        return (Colors.CYAN if self.color == "CYAN" else Colors.GREEN if self.color == "GREEN" else Colors.RED)


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