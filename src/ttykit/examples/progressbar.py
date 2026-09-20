from ttykit.progress import Progress
from ttykit.data._state import BARS
from time import sleep

def show_all_bars():
    for name in BARS.keys():
        with Progress(total=100, prefix="Test Bar", bar_style=name) as bar:
            sleep(2)
            bar.advance(25)


if __name__ == "__main__":
    show_all_bars()