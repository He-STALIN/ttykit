class TTYError(Exception):
    """Base error for all ttykit exceptions"""


class PagingError(TTYError):
    """Raised when paging is disabled but a page operation is attempted"""


class RenderError(TTYError):
    """Raised when rendering fails"""


class CallableError(TTYError):
    """Raised when type not is callable"""