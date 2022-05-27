import pytest
import os
import filecmp
from src.test4.task1.logger import logger
import re


def test_logger():
    @logger(handle="my_log.txt")
    def f(n):
        if n != 0:
            f(n - 1)

    f(1)
    with open("my_log.txt") as file:
        inp = re.split(" |\n", file.read())
        print(inp)
    assert len(inp) == 13
    data1 = "".join(inp[2:6])
    data2 = "".join(inp[8:12])
    assert data1 == "f(0,){}None"
    assert data2 == "f(1,){}None"
    os.remove("my_log.txt")
