import functools
from typing import Callable, Union


def safe_call(func: Callable = None, *, handle: str = "default.txt") -> Callable:
    if func is None:
        return lambda func: safe_call(func, handle=handle)

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Union[Callable, None]:
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            with open(handle, "a") as log:
                log.write(
                    f"Error in function: {func.__name__}; with args: {args}; kwargs: {kwargs}; with message: {ex}\n"
                )
            return None

    return inner
