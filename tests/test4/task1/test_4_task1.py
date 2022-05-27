import pytest
import os
import filecmp
from src.test4.task1.logger import logger
import re


def test_logger_with_one_arg():
    @logger(handle="my_log.txt")
    def f(n):
        if n != 0:
            f(n - 1)

    f(1)
    with open("my_log.txt") as file:
        inp = re.split(" |\n", file.read())
    assert len(inp) == 13
    data1 = "".join(inp[2:6])
    data2 = "".join(inp[8:12])
    assert data1 == "f(0,){}None"
    assert data2 == "f(1,){}None"
    os.remove("my_log.txt")


def test_logger_with_kwargs_and_return():
    @logger(handle="my_log.txt")
    def f(n, named):
        if n != 0:
            f(n - 1, named=named)
        return n * named

    f(1, named="wer")
    with open("my_log.txt") as file:
        inp = re.split(" |\n", file.read())
    assert len(inp) == 15
    data1 = "".join(inp[2:7])
    data2 = "".join(inp[9:15])
    assert data1 == "f(0,){'named':'wer'}"
    assert data2 == "f(1,){'named':'wer'}wer"
    os.remove("my_log.txt")
