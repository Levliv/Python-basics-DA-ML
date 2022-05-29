import pytest
import os
from src.test3.task1.sprites import generator


def test_file():
    generator(8, 8, 7, 3, "test.png")
    assert os.path.exists("test.png")
    os.remove("test.png")
