import re
from .data._state import Styles, Colors


class Segmentation:
    """Split text into non-empty pieces using a regular expression."""

    def __init__(self, text: str, separator: str = r"\s+"):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        if not isinstance(separator, str):
            raise TypeError("separator must be a regular expression string")

        re.compile(separator)
        self.text = text
        self.separator = separator

    def segment(self) -> list[str]:
        """Return text pieces separated by the configured regular expression."""
        return [
            piece.strip()
            for piece in re.split(self.separator, self.text)
            if piece.strip()
        ]

    def __call__(self) -> list[str]:
        """Segment the stored text."""
        return self.segment()

    def _apply_tag(self, tag: str, stack: list):
        clean = tag.strip("[]").split()
        for t in clean:
            if t == "/":
                stack.clear()
            elif t.startswith("/"):
                name = t[1:]
                if name in stack:
                    stack.remove(name)
            else:
                stack.append(t)

    def _get_ansi_from_stack(self, stack: list) -> str:
        ansi = ""
        for style in stack:
            ansi += Colors.get(style, "") + Styles.get(style, "")
        return ansi

    def auto_compile(self) -> str:
        result = ""
        style_stack = []
        pos = 0
        last_ansi = ""

        for match in re.finditer(r"\[/?\w*(?:\s+\w+)*\]", self.text):
            # Текст до тега
            if match.start() > pos:
                result += self.text[pos:match.start()]

            # Обработка тега
            tag = match.group()
            self._apply_tag(tag, style_stack)

            # Сброс предыдущих ANSI и применение новых
            new_ansi = self._get_ansi_from_stack(style_stack)
            if new_ansi != last_ansi:
                result += Styles.RESET + new_ansi
                last_ansi = new_ansi

            pos = match.end()

        # Остаток текста
        if pos < len(self.text):
            result += self.text[pos:]

        result += Styles.RESET
        return result

    def clean_tag(self, tag: str) -> list:
        """
        Очищает тег от лишних символов и возвращает список стилей.
        
        Пример:
            "[blue bold]" -> ["blue", "bold"]
            "[/red]"      -> ["/red"]
            "[/]"         -> ["/"]
        """
        # Убираем квадратные скобки
        tag = tag.strip("[]")
        
        # Разбиваем по пробелам
        parts = tag.split()
        
        # Убираем пустые строки
        parts = [p for p in parts if p]
        
        return parts