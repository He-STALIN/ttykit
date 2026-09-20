import keyboard as kb
import os, sys


class TUI:
    """
    Create TUI (Text User Interface) in terminal with user menus

    Args:
        title (str): title of the `TUI`

    ### Methods:
        `addMenu(name, callback)`: add menu to UI render.
        `Run()`: exec and start render the UI.
        `UpdateUI()`: forced update UI Layer.

    ### Examples

    ```python
    from ttykit import TUI

    ui = TUI("this example UI!")

    def someAction():
        # do something

    ui.addMenu("Us menu", someAction) # adding menu in UI

    ui.Run() # and start render UI
    ```
    Out in Terminal
    ```
    ===[ this example UI! ]===

        > Us menu

        > Exit
    
    For control use arrows Up/Down and Enter to select
    ```
    """
    def __init__(self, title: str):
        super().__init__()

        print("[WARNING] Class 'TUI' not fully completed and may contain errors.")

        self.TITLE: str = title if title else "Text UI"
        self.FOOTER: str = "For control use arrows Up/Down and Enter to select"
        self.DEFAULT_SPACE = "   "
        self._requestClosing: bool = False
        self.action: int = 1
        self._max_menus: int = 0
        self._menus: list = []
        kb.add_hotkey("Up", self._UpMenu)
        kb.add_hotkey("Down", self._DownMenu)
        kb.add_hotkey("enter", self._selectAction)

    def _clearTerminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _selectAction(self):
        if self.action == self._max_menus:
            self._requestClosing = True
            return
        
        menu = self._menus[self.action - 1]
        menu["callback"]()

    def _UpMenu(self):
        self.action -= 1

        if self.action < 1:
            self.action = self._max_menus

        self.UpdateUI()

    def _DownMenu(self):
        self.action += 1

        if self.action > self._max_menus:
            self.action = 1

        self.UpdateUI()

    def UpdateUI(self):
        """Update UI Layer in Terminal"""
        TUI = ""
        TUI += f"===[ {self.TITLE} ]==="
        TUI += "\n\n"

        _current_menu = 1
        for menu in self._menus:
            if self.action == _current_menu:
                TUI += f"{self.DEFAULT_SPACE}\033[34m> {menu["name"]}\033[0m\n"
            else:
                TUI += f"{self.DEFAULT_SPACE}> {menu["name"]}\033[0m\n"

            TUI += "\n"
            _current_menu += 1

        if len(self._menus) == self._max_menus:
            self._max_menus += 1 #? add Exit menu in UI
        
        if self.action == self._max_menus: #? exit menu always is last
            TUI += f"{self.DEFAULT_SPACE}\033[31m> Exit\033[0m\n"
        else:
            TUI += f"{self.DEFAULT_SPACE}> Exit\033[0m\n"

        TUI += "\n" + self.FOOTER + "\n"

        sys.stdout.write("\033[H") #? set cursor to pos (0, 0)
        sys.stdout.write(TUI)
        sys.stdout.flush()

    def addMenu(self, name: str, callback):
        """
        Adding menu to UI.

        Args:
            name (str): name of the menu
            callback: what need to call, when menu selected
        """
        try:
            self._menus.append({
                "name": name,
                "callback": callback
            })
            self._max_menus += 1
        except Exception as e:
            raise Exception(e)

    def Run(self):
        if len(self._menus) < 1:
            raise ValueError("UI can't has been created without menus")
        
        try:
            self._clearTerminal()
            self.UpdateUI()
            while True:
                if self._requestClosing:
                    sys.exit()
                    break
                else:
                    pass
        
        except KeyboardInterrupt:
            sys.stdout.write("[!] Exited by user\n")
            sys.stdout.flush()

        except Exception as e:
            raise Exception(e)