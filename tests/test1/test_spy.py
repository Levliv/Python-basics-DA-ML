import pytest
from .src.test1.spy import *


def simple_test():
    @Spy
    def first(x):
        return x

    first(3)
    res = print_usage_statistic(first)
    assert res[0][1] == {'args': (3,), 'kwargs': {}}


def exception():
    def no_dec(r):
        return r
    with pytest.raises(TypeError) as ex:
        print_usage_statistic(no_dec)
        assert 'function to load history must be decorated with Spy' in str(ex.value)