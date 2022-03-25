from datetime import *
from typing import *
from copy import deepcopy
from functools import update_wrapper


class Spy:
    """
    Functions launch history saver.
    """

    def __init__(self, func: Callable):
        self.func = func
        self.hist = []
        update_wrapper(self, func)

    def __call__(self, *args: Any, **kwargs: Any):
        self.hist.append((datetime.now(), {"args": args, "kwargs": kwargs}))
        return self.func(*args, **kwargs)


def print_usage_statistic(func: Callable):
    """
    Launching history getter.
    """
    if isinstance(func, Spy):
        return func.hist
    else:
        raise TypeError("function to load history must be decorated with Spy")
