import traceback, sys
from ttykit import data

def custom_excepthook(exc_type, exc_value, exc_tb):
    tb_lines = traceback.format_exception(exc_type, exc_value, exc_tb)
    
    # Самая длинная строка
    error_line = f"Error: {exc_type.__name__}"
    msg_line = f"Message: {exc_value}"
    max_len = max(len(error_line), len(msg_line), 40)
    
    # Рамка
    print(f"╔{'═' * (max_len + 4)}╗")
    print(f"║  {data.Colors.RED}{error_line.ljust(max_len)}{data.RESET}  ║")
    print(f"║  {data.Colors.RED}{msg_line.ljust(max_len)}{data.RESET}  ║")
    print(f"╠{'═' * (max_len + 4)}╣")
    
    for line in tb_lines[-3:]:
        clean = line.strip()
        if len(clean) > max_len:
            clean = clean[:max_len-3] + "..."
        print(f"║  {clean.ljust(max_len)}  ║")
    
    print(f"╚{'═' * (max_len + 4)}╝")

def set_custom_hook(Traceback: bool=False) -> None:
    """
    Set a custom methods

    Args:
        Traceback (bool): replace Traceback on custom or not. Default `False`
    """

    print("[WARNING] this method 'set_custom_hook' unstable and may not working")

    if Traceback:
        print('set custom excepthook...')
        sys.excepthook = custom_excepthook