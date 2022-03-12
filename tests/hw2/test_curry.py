import pytest
import directory_handler

from src.hw2.partial import curry_explicit, uncurry_explicit

def test_answer():
    args = (123, 456, 562)
    res = curry_explicit(lambda x, y, z: f"<{x}, {y}, {z}>", 3)
    for i in range(3):
        res = res(args[i])
    assert res == "<123, 456, 562>"
