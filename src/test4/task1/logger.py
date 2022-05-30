import functools
import datetime
from typing import Callable


def logger(func: Callable = None, *, handle: str = "default.txt") -> Callable:
    if func is None:
        return lambda func: logger(func, handle=handle)

    @functools.wraps(func)
    def inner(*args, **kwargs) -> None:
        with open(handle, "a") as log:
            log.write(
                f"{datetime.date.today()} {datetime.datetime.now().time()} {func.__name__} {args} {kwargs} {func(*args, **kwargs)}\n"
            )
        return None

    return inner
