import pytest
from src.tests.test2.takes import *


def simple_test():
    @taskes(int)
    def first(num):
        return num

    with pytest.raises(TypeError) as ex:
        first("abc")
        assert "should have another type" in str(ex.value)


def correct_args_test():
    @taskes(int, int)
    def first(f, s):
        return max(f, s)

    assert first(2, 5) == max(2, 5)


def less_args_test():
    @takes(int, int)
    def first(f, s, t):
        return max(f, s, t)

    with pytest.raises(TypeError) as ex:
        first(2, "a", 4)
        assert "should have another type" in str(ex.value)
