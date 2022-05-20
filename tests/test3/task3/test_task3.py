import pytest
import os
from src.test3.task3.safe_func_decorator import safe_call


def test_func_without_error():
    @safe_call(handle="test_error.txt")
    def identity(i, j):
        return i * j

    value = identity(2, 3)
    assert value == 6
    assert os.path.exists("test_error.txt") == False


def test_func_with_args_and_kwargs_with_error():
    @safe_call(handle="test.txt")
    def identity(i, j=5):
        raise IndexError("example_error")

    value = identity(2, j=4)
    with open("test.txt", "r") as file:
        expected = "Error in function: identity; with args: (2,); kwargs: {'j': 4}; with message: example_error\n"
        assert expected == file.read()
    assert value is None
    os.remove("test.txt")


def test_func_with_args_with_error():
    @safe_call(handle="test.txt")
    def identity(i, j):
        raise IndexError("example_error")

    value = identity(2, 3)
    with open("test.txt", "r") as file:
        expected = "Error in function: identity; with args: (2, 3); kwargs: {}; with message: example_error\n"
        assert expected == file.read()
    assert value is None
    os.remove("test.txt")


def test_several_functions():
    @safe_call(handle="test.txt")
    def first(i, j):
        raise IndexError("first_error")

    @safe_call(handle="test.txt")
    def second(i, j):
        return i * j

    @safe_call(handle="test.txt")
    def third(i, j):
        raise IndexError("third_error")

    value1 = first(1, 3)
    value2 = second(2, 5)
    value3 = third(4, 8)
    with open("test.txt", "r") as file:
        expected = (
            "Error in function: first; with args: (1, 3); kwargs: {}; with message: first_error\n"
            "Error in function: third; with args: (4, 8); kwargs: {}; with message: third_error\n"
        )
        assert expected == file.read()
    assert value2 == 10
    os.remove("test.txt")
