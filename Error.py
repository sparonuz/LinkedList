class Error(Exception):
    """Base class for other exceptions"""
    pass
class KeyNotFound(Error):
    """Raised when find function fail"""
    pass
class EmptyLinkedList(Error):
    """Raised when Linked List is empty"""
    pass