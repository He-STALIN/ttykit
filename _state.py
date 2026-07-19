from enum import Enum

class Colors:
    """Applied colors for text in the terminal. Can be mixed with `class Style`"""
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    DARK_GREY = "\033[90m"
    LIGHT_RED = "\033[91m"
    LIGHT_GREEN = "\033[92m"
    LIGHT_YELLOW = "\033[93m"
    LIGHT_BLUE = "\033[94m"
    LIGHT_PURPLE = "\033[95m"
    LIGHT_CYAN = "\033[96m"
    LIGHT_WHITE = "\033[97m"
    RESET = "\033[0m"

class Styles:
    """Applied styles for text in the terminal. Can be mixed with `class Colors`"""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    RAPID_BLINK = "\033[6m"
    REVERSE = "\033[7m"
    STRIKETHROUGH = "\033[9m"

RESET = "\033[0m"

class TaskState(Enum):
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"

ANIMATION = {
    'bar': ["[      ]", 
            "[=     ]", 
            "[==    ]",
            f"[{Colors.RED}*{RESET}==   ]", 
            f"[={Colors.RED}*{RESET}==  ]", 
            f"[=={Colors.RED}*{RESET}== ]", 
            f"[ =={Colors.RED}*{RESET}==]", 
            f"[  =={Colors.RED}*{RESET}=]", 
            f"[   =={Colors.RED}*{RESET}]", 
            "[    ==]", 
            "[     =]", 
            "[      ]"
        ],
    'ball':["(●     )", 
            "( ●    )", 
            "(  ●   )", 
            "(   ●  )", 
            "(    ● )", 
            "(     ●)", 
            "(    ● )", 
            "(   ●  )", 
            "(  ●   )", 
            "( ●    )"
            ],
    'dots': ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
    'dots12':  ["⢀⠀", 
                "⡀⠀", 
                "⠄⠀", 
                "⢂⠀", 
                "⡂⠀", 
                "⠅⠀", 
                "⢃⠀", 
                "⡃⠀", 
                "⠍⠀", 
                "⢋⠀", 
                "⡋⠀", 
                "⠍⠁", 
                "⢋⠁", 
                "⡋⠁", 
                "⠍⠉", 
                "⠋⠉", 
                "⠋⠉", 
                "⠉⠙", 
                "⠉⠙", 
                "⠉⠩", 
                "⠈⢙", 
                "⠈⡙", 
                "⢈⠩", 
                "⡀⢙", 
                "⠄⡙", 
                "⢂⠩", 
                "⡂⢘", 
                "⠅⡘", 
                "⢃⠨", 
                "⡃⢐", 
                "⠍⡐", 
                "⢋⠠", 
                "⡋⢀", 
                "⠍⡁", 
                "⢋⠁", 
                "⡋⠁", 
                "⠍⠉", 
                "⠋⠉", 
                "⠋⠉", 
                "⠉⠙", 
                "⠉⠙", 
                "⠉⠩", 
                "⠈⢙", 
                "⠈⡙", 
                "⠈⠩", 
                "⠀⢙", 
                "⠀⡙", 
                "⠀⠩", 
                "⠀⢘", 
                "⠀⡘", 
                "⠀⠨", 
                "⠀⢐", 
                "⠀⡐", 
                "⠀⠠", 
                "⠀⢀", 
                "⠀⡀"
                ],
    'bouncingBar': ["[      ]", 
                    "[=     ]", 
                    "[==    ]", 
                    f"[{Colors.RED}*{RESET}==   ]", 
                    f"[={Colors.RED}*{RESET}==  ]", 
                    f"[=={Colors.RED}*{RESET}== ]", 
                    f"[ =={Colors.RED}*{RESET}==]", 
                    f"[  =={Colors.RED}*{RESET}=]", 
                    f"[   =={Colors.RED}*{RESET}]", 
                    "[    ==]", 
                    "[     =]", 
                    "[      ]", 
                    "[     =]", 
                    "[    ==]", 
                    f"[   =={Colors.RED}*{RESET}]", 
                    f"[  =={Colors.RED}*{RESET}=]", 
                    f"[ =={Colors.RED}*{RESET}==]", 
                    f"[=={Colors.RED}*{RESET}== ]", 
                    f"[={Colors.RED}*{RESET}==  ]", 
                    f"[{Colors.RED}*{RESET}==   ]", 
                    "[==    ]", 
                    "[=     ]", 
                    "[      ]"
                    ],
    'points': ["∙∙∙", "●∙∙", "∙●∙", "∙∙●", "∙∙∙"],
    'wave': [" ~ ", " ≈ ", " ≈≈", "≈≈≈", "≈≈ ", " ≈ ", " ~ "],
    'pulse': [" • ", " ••", "•••", "•• ", " • "],
    'moon': ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"],
    'clock':["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"],
    'snake': ["➡", "⬆", "⬅", "⬇"],
    'line': ["|", "/", "-", "\\"],
    'box': ["▖", "▘", "▝", "▗"],
    'arc': ["◜", "◠", "◝", "◞", "◡", "◟"]
}