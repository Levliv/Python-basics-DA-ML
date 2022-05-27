import pytest
import os
import filecmp
from src.test4.task1.logger import logger
import re


def test_logger():
    @logger(handle='my_log.txt')
    def f(n):
        if n != 0:
            f(n - 1)

    f(1)
    with open('my_log.txt') as file:
        inp = re.split(' |\n', file.read())
        print(inp)
    assert len(inp) == 13
    os.remove('my_log.txt')

