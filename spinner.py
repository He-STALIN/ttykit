import time
from .status import Status, TaskState
from ._state import STATUS_ANIMATION

def show_all_spinners():
    for name in STATUS_ANIMATION.keys():
        print(f"-==[ {name} ]==-")
        with Status("Test", spinner=name) as status:
            time.sleep(2)
            status.set_state(TaskState.SUCCESS)

if __name__ == "__main__":
    show_all_spinners()