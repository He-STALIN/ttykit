import time
from .status import CustomStatus, TaskState
from ._state import ANIMATION

def show_all_spinners():
    for name in ANIMATION.keys():
        print(f"-==[ {name} ]==-")
        with CustomStatus("Test", spinner=name) as status:
            time.sleep(2)
            status.set_state(TaskState.SUCCESS)

if __name__ == "__main__":
    show_all_spinners()