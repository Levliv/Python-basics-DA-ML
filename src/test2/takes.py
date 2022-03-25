from typing import *
import inspect
from copy import deepcopy


def takes(*types):
    return lambda func: checker(func, *types)


def checker(func: Callable, *types: object):
    def inner(*args, **kwargs):
        sign = inspect.signature(func)
        arg = list(deepcopy(*args))
        for x, y in sign.parametrs.item():
            if x in kwargs:
                arg.append(kwargs[x])
        map(lambda data, type: ex_raiser(data, type), arg, types)

    def ex_raiser(data, type):
        if not isintance(data, type):
            raise TypeError(f"{data} should have another type")

    return inner
