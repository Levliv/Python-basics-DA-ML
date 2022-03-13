from contextlib import contextmanager
from threading import Lock


class ConcurrentDict:
    """Safe for multi threading dict"""

    def __init__(self):
        self.dict = dict()
        self.locker = Lock


@contextmanager
def modify_safely(self):
    """Safe dictionary modifier"""
    self.locker.acquire()
    try:
        yield self.dict
    finally:
        self.locker.release()
