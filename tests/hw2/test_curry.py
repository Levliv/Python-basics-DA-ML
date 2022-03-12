import pytest
from src.hw2.partial import curry_explicit, uncurry_explicit


def test_curry():
    args = (123, 456, 562)
    res = curry_explicit(lambda x, y, z: f"<{x}, {y}, {z}>", 3)
    for i in range(3):
        res = res(args[i])
    assert res == "<123, 456, 562>"


def test_curry_negative_arity():
    with pytest.raises(RuntimeError):
        curry_explicit(sum, -1)


def test_curry_zero_args():
    func = curry_explicit(lambda: 1, 0)
    assert func() == 1


def test_curry_more_real_args():
    with pytest.raises(TypeError or RuntimeError):
        func = curry_explicit(sum, 2)
        func(1)(2)(3)


def test_uncurry():
    args = (123, 456, 562)
    func = curry_explicit(lambda x, y, z: f"<{x}, {y}, {z}>", 3)
    res = uncurry_explicit(func, 3)
    assert res(*args) == "<123, 456, 562>"


def test_uncurry_negative_arity():
    func = curry_explicit(sum, 2)
    with pytest.raises(RuntimeError):
        uncurry_explicit(func, -1)


def test_uncurry_more_real_args():
    func = curry_explicit(sum, 2)
    uncurried = uncurry_explicit(func, 2)
    with pytest.raises(RuntimeError):
        uncurried(1, 2, 3)
