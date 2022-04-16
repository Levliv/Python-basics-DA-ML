import pytest
from src.hw4.Tree import Treap, TreapNode


def test_contains():
    base = {i: i for i in range(7)}
    treap = Treap(base)
    for i in range(7):
        assert i in treap
    assert -1 not in treap


def test_find_node():
    base = {i: i for i in range(7)}
    treap = Treap(base)
    assert treap.find(0).value == 0
    assert 0 in treap


def test_iter_get_set():
    base = {i: i for i in range(7)}
    treap = Treap(base)
    assert treap[1] == 1
    treap[1] = 1
    assert treap[1] == 1


def test_delitem():
    base = {i: i for i in range(7)}
    treap = Treap(base)
    del treap[1]
    assert 1 not in treap
    assert 2 in treap
