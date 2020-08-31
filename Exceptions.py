class Error(Exception):
    """Base class for other exceptions"""
    pass


class MaxFrameExceededError(Error):
    """Raised when the input value is too small"""
    pass


class checkLastFrameValError(Error):
    """Raised when the input value is too large"""
    pass
