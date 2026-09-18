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

    def get(name: str = None, default: str = None) -> str:
        """Return the color ANSI code from color name

        Args:
            name (str): name of color
            default (str | None): what will be return if color not found
        Returns:
            color (str): ANSi code of color
        """
        match name.lower():
            case "black": return Colors.BLACK
            case "red": return Colors.RED
            case "green": return Colors.GREEN
            case "yellow": return Colors.YELLOW
            case "blue": return Colors.BLUE
            case "purple": return Colors.PURPLE
            case "cyan": return Colors.CYAN
            case "white": return Colors.WHITE
            case "dark_grey": return Colors.DARK_GREY
            case "light_red": return Colors.LIGHT_RED
            case "light_green": return Colors.LIGHT_GREEN
            case "light_yellow": return Colors.LIGHT_YELLOW
            case "light_blue": return Colors.LIGHT_BLUE
            case "light_purple": return Colors.LIGHT_PURPLE
            case "light_cyan": return Colors.LIGHT_CYAN
            case "light_white": return Colors.LIGHT_WHITE
            case _: return default

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

    def get(name: str = None, default: str = None) -> str:
        """Return the style ANSI code from style name
        
        Args:
            name (str): name of style
            default (str | None): what will be return if style not found
        Returns:
            style (str): ANSi code of style
        """
        match name.lower():
            case "bold": return Styles.BOLD
            case "dim": return Styles.DIM
            case "italic": return Styles.ITALIC
            case "underline": return Styles.UNDERLINE
            case "blink": return Styles.BLINK
            case "rapid_blink": return Styles.RAPID_BLINK
            case "reverse": return Styles.REVERSE
            case "strikethrough": return Styles.STRIKETHROUGH
            case "reset": return Styles.RESET
            case _: return default

RESET = "\033[0m"

class TaskState(Enum):
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"

STATUS_ANIMATION = {
    'bar': ["[      ]", 
            "[=     ]", 
            "[==    ]",
            f"[{Colors.RED}*{RESET}==   ]", 
            f"[={Colors.RED}*{RESET}==  ]", 
            f"[=={Colors.RED}*{RESET}== ]", 
            f"[ =={Colors.RED}*{RESET}==]", 
            f"[  =={Colors.RED}*{RESET}=]", 
            f"[   =={Colors.RED}*{RESET}]{RESET}", 
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

BARS = {
    'line': {
        "filled": f"{Colors.LIGHT_PURPLE}━{RESET}",
        "bg": f"{Colors.DARK_GREY}━{RESET}"
    },
    'points': {
        "filled": "●",
        "bg": f"{Colors.DARK_GREY}○{RESET}"
    },
    'blocks': {
        "filled": "█",
        "bg": "░"
    },
    "arrow": {
        "filled": f"{Colors.GREEN}═{RESET}",
        "bg": f"{Colors.DARK_GREY}-{RESET}"
    }
}
