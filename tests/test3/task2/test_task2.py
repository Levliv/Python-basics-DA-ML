import pytest
from src.test3.task2.html_manager import *
import filecmp
import os


def test_example():
    html = HTML()
    with html.body():
        with html.div():
            with html.div():
                html.p("first string.")
                html.p("second string.")
            with html.div():
                html.p("Third string.")
    html.generate('test.txt')
    assert filecmp.cmp("tests/test3/task2/expected.txt", "src/test3/task2/test.txt")
    os.remove("src/test3/task2/test.txt")
