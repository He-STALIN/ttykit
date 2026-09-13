<div align="center">

# HOW TO USE
**Examples of code**
</div>

# Beforehand
- ttykit have 5 classes with their appointments:
    - `Console` [GO](#console-class)
        > Terminal controls
    - `Status` [GO](#status-class)
        > showing status
    - `Progress` [GO](#progress-class)
        > showing progress execution
    - `TUI` [GO](#tui-class)
        > show interface
    - `Tree` [GO](#tree-class)
        > compile structure in tree view
- Also have utility classes:
    - `TaskState` [GO](#taskstate-class)
    - `Colors` [GO](#colors-class)
    - `Styles` [GO](#styles-class)

- Well, let's go next

# Code Examples

## `Console` class
> How said upper, this class controlling events in terminal.
>
> to start use, write
```python
from ttykit import Console

console = Console() # getting instance of class to next uses
```
> Next code examples for this class they will base their work on this code.
> 
> This class can getting 6 args:
- `color_system` (str, optional)
    > Color system of the terminal. Default is "auto".
    >
    > Can be "standard", "256" or "truecolor". If you don't know what use, lease as "auto" to autodetect

- `width` (int)
    > Width of the terminal.
    >
    > You can set custom width or leave as `None` to autodetect current width.

- `height` (int)
    > height of the terminal.
    >
    > How `width` too, you can set custom height or lease as `None` to autodetect.

- `stderr` (bool)
    > Control where print error.
    > 
    > If active, errors will be writed to stdErr instead stdOut, else to stdOut.

- `no_color` (bool)
    > Controls color in terminal.
    >
    > If active, all will be monochrome (black and white) without other colors.

- `force_terminal` (bool)
    > If active, lib does not check terminal and will be use control codes in any situation.

> So, class have 3 methods:

- `bell()`
    > It send event signal to playing bell sound. equivalent to the ANSI code `\a`.
    >
    > I think, for this method example not needed.

- `print(*args, sep, end, justify, fillchar)`
    > print text in stream of the terminal.
    > 
    > It can getting 5 args:
    - `*args`
        > just your string, that you want to output
    - `sep` (str)
        > separator symbol if you give some strings. Default is " " (space).
    - `end` (str)
        > symbol of end printing. Default is new line symbol (`\n`).
    - `justify` (str)
        > Justifying text in output. Can be "left", "center", "right". Default is "left".
    - `fillchar` (str)
        > char for filling free space in terminal. Usually this not set, because default is " " (space).

        ```python
        text = "Your some text for [green] output [/]"

        console.print(text, justify="left")
        ```
    > Yeah, You might have noticed `[green]` and `[/]`
    > 
    > This is templates to insert colors and styles. For the insertion to work, the name must be in `[ ]`. And do not not forged add "[/]" in end of string, else next symbols will have your stylistics.
    >
    > In one template (`[ ]`) you can set color and style together.
    > 
    > Available colors to insert: `black`, `red`, `green`, `yellow`, `blue`, `purple`, `cyan`, `white`, `dark_grey`, `light_red`, `light_green`, `light_yellow`, `light_blue`, `light_purple`, `light_cyan`, `light_white`
    >
    > Available styles to insert: `bold`, `dim`, `italic`, `underline`, `blink`, `rapid_blink`, `reverse`, `strikethrough`


- `input(prompt, password)`
    > Getting writed data by user.
    >
    > it can getting args:
    - `prompt` (str)
        > prompt (or hint) for user. You can not set this (is optional).
    - `password` (bool)
        > If this flag actived, writed by user data will be hidded in terminal (disable echo char).
        ```python
        input = console.input("some prompt", password=True) # says "Hey, hide symbols"
        ```
    > You can also use templates colors and styles here.

## `Status` class
> This class showing animated status, while your code executes payload.
>
> To start use this class, write
```python
from ttykit import Status
```
> But there class have 2 ways to realization:
>
> 1. Create one instance to all your code
```python
status_inst = Status()
```
> 2. Use context manager to individual
```python
with Status() as status:
    ...
```
> Well, with realization we finished.
>
> This class can getting 3 args:
- `message` (str)
    > Name or description of execution unit. Just to clarify "what's working right now"
    >
    > You can if get it, or leave as empty.

- `spinner` (str)
    > spinner of animated status. default is "bar"
    >
    > Available spinners: `bar`, `ball`, `dots`, `dots12`, `bouncingBar`, `points`, `wave`, `pulse`, `moon`, `clock`, `snake`, `line`, `box`, `arc`.
    >
    > don't know, what select? You can see animation: exec `python -m ttykit.spinner`

- `color` (str)
    > color for #message arg text selection.
    >
    > Available colors already sayed upper in `Console.print()`
> Okay, let's we see methods, and next i describe examples.
>
> This class presents 4 methods:
- `set_message(new_message)`
    > replace old message of task to new.
    >
    > This is useful if you implemented the solution using the first approach.
    >
    > It receives a string as an argument.

- `set_state(state)`
    > Set the state of task execution.
    >
    > For set this, you need use `TaskState` (have in this lib)

- `pause()`
    > Set animation to pause. Nothing more.

- `resume()`
    > Resume animation. Nothing more.

> So, we've reached to the examples.
>
> I show 2 example for 2 approach
>
> First approach
```python
from ttykit import TaskState

with status as status:
    status.set_message("some unit") #set name for this
    <your some payload>
    status.set_state(TaskState.SUCCESS) # set status file finished

with status as status:
    status.set_message("some unit 2")
    ...
```
> There we create status of task from instance.
>
> This implementation allows for optimized memory usage when the status of multiple tasks needs to be displayed.
>
> TaskState is utility class, so i will describe it in the end.
>
> Second approach
```python
from ttykit import TaskState

with Status("unit name", spinner="dots12") as status:
    <some payload>
    status.set_state(TaskState.SUCCESS)

with Status("unit name 2", spinner="dots12") as status:
    <some payload 2>
    status.set_state(TaskState.SUCCESS)
```
> There we create of task from main class (through context manager)
>
> If memory usage is not critical, you can use this implementation.

## `Progress` class
> Upper i already said, what this class create progress bar in terminal.
>
> To use this, write
```python
from ttykit import Progress
```
> Here, how in [`Status class`](#status-class) too, have 2 ways, but describe theь again i will not.
>
> Let's seen arguments, which it accept:
- `total` (int)
    > max value of bar. Default is `100`
- `prefix` (str)
    > this set some description for bar. Just for clarity
    >
    > can be empty
- `bar_length` (int)
    > length of the bar in symbols. Default is `30`
- `bar_style` (str)
    > Stylistic of the bar. Default is `line`
    >
    > Available styles; `line`, `points`, `blocks`, `arrow`.
- `frames` (bool)
    > If active, adding brackets to bar. Default is `False`
- `show_ETA` (bool)
    > If active, next to bar will be show ETA (Estimated Time of Arrival). Default is `True`
> And have 4 methods:
- `update(value)`
    > set current value for the bar. Value require is Integer
- `advance(step)`
    > update current value on *n* steps. Step require is Integer.
    >
    > Unlike `Update`, `Advance` adds to the progress rather than setting it.
- `stop()`
    > force stopping bar render and exiting.
- `finish()`
    > Set value to 100% and exiting.

> Well, the implementation is similar to implementation in `Status class`, just args is more.
>
> I will show only one example of implementation. I hope, you understand, how create other implementation.
```python
with Progress(total=100, prefix="Loading from Internet", bar_length=60) as bar:
    for i in range(100)
        bar.advance(1)
```
> For example i use cycle "for", but you will need realization with the payload


## `TUI` class
> Provides methods to render Text UI in terminal
>
> Now class not fully completed and may contain errors. In next version i will try refine logic.
>
> So, to use, write
```python
from ttykit import TUI

ui = TUI(title="simple UI")
```
> We init class instance, but now it empty.
>
> `TUI` getting string for UI title. in example i set "simple UI" how title
>
> First i will show Available methods:
- `addMenu(name, callback)`
    > It add your item to interface.
    >
    > Name is string
    >
    > Callback is your func, which will called if user select this action
    ```python
    def your_callback():
        pass

    ui.addMenu("test item", callback)
    ```
- `UpdateUI()`
    > force updating UI.
    > 
    > Useful if you add new item while menu working.
- `Run()`
    > Okay, we added Items to UI and setup logic, but menu not showed.
    > 
    > For exec menu, you need call this method: it calculate data and compile first render of UI.
> That's all, what can do this class, but in future will can more.
>
> Full example
```python
from ttykit import TUI

def read();
    print("reading")

def set_star():
    print("repository is starred")

ui = TUI(title="simple UI")
ui.addMenu("read documentation", read)
ui.addmenu("set star to repositoty on GitHub", set_star)

ui.Run()
```

## `Tree` class
> This class help create tree structure in terminal
>
> To use, write (How many times have I written this?)
```python
from ttykit import Tree

tree = Tree(label="Example of tree")
```
> And have 2 methods:
- `add(label)`
    > Add node to tree and return instance.
    >
    > Yeah, it's just create clone of `Tree` to create node.
    ```python
    tree.add("pyproject.toml")
    tree.add("REAMDE.md")
    ...
    ```
    > And you can make ierachy:
    ```python
    src = tree.add("src")
    src.add("__init__.py")
    src.add("main.py")
    ...
    ```
- `print()`
    > When you set all nodes to tree, call this method to print all structure.
> That's all. Class not defficulty, right?
>
> Full Example
- `code`
    ```python
    from ttykit import Tree

    tree = Tree('Tree example')
    tree.add("pyproject.toml")
    tree.add("README.md")
    src = tree.add("src")
    src.add("main.py")
    src.add("decorators.py")

    tree.print()
    ```
- `Output`
    ```text
    Tree example
    ├── pyproject.toml
    ├── README.md
    └── src
        ├── main.py
        └── decorators.py
    ```


---

## `TaskState` class
> This class inherits Enum and have 4 vars
- `RUNNING`
    > return running code from Enum and have value "running"
- `SUCCESS`
    > return success code from Enum and have value "success"
- `ERROR`
    > return error code from Enum and have value "error"
- `WARNING`
    > return warning code from Enum and have value "warning"
> I don't know what say, i create it for correct recieving states


## `Colors` class
> provides ANSI codes of colors. Available:
- `BLACK`
- `RED`
- `GREEN`
- `YELLOW`
- `BLUE`
- `PURPLE`
- `CYAN`
- `WHITE`
- `DARK_GREY`
- `LIGHT_RED`
- `LIGHT_GREEN`
- `LIGHT_YELLOW`
- `LIGHT_BLUE`
- `LIGHT_PURPLE`
- `LIGHT_CYAN`
- `LIGHT_WHITE`
> And have method `get()` to get code from color name.


## `Styles` class
> provides ANSi codes of text styles. Available:
- `BOLD`
- `DIM`
- `ITALIC`
- `UNDERLINE`
- `BLINK`
- `RAPID_BLINK`
- `REVERSE`
- `STRIKETHROUGH`
> and too have method `get()` to get code from style name