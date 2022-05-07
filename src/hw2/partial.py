from typing import Callable, Any


def curry_explicit(func: Callable, arity: int) -> Callable:
    """
    Returns curried function.
    """
    if arity < 0:
        raise RuntimeError("Arity should be positive")
    if arity < 2:
        return func

    def curry(arg: Any) -> Callable:
        def simplify(*args):
            if len(args) != arity - 1:
                raise RuntimeError("Curry: Arity doesn't match with the number of args")
            return func(arg, *args)

        return curry_explicit(simplify, arity - 1)

    return curry


def uncurry_explicit(func: Callable, arity: int) -> Callable:
    """
    Returns function with the number of args defined in arity.
    """
    if arity < 0:
        raise RuntimeError("Arity should be positive")
    if arity == 0:
        return func

    def uncurry(*args: Any) -> Callable:
        if len(args) != arity:
            raise RuntimeError("Uncurry: Arity doesn't match with the number of args")
        res = func
        for arg in args:
            res = res(arg)
        return res

    return uncurry
