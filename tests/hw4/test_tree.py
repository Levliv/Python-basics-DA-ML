import pytest
from src.hw4.Tree import Treap, TreapNode


def test_empty_treap():
    with pytest.raises(TypeError):
        treap = Treap({})


def test_contains():
    base = {i: i for i in range(7)}
    treap = Treap(base)
    for i in range(7):
        assert i in treap.root
    assert -1 not in treap.root


def test_iter_get_set():
    base = {i: i for i in range(7)}
    treap = Treap(base)
    assert treap[1] == 1
    treap[1] = 'a'
    assert treap[1] == 'a'


def test_delitem():
    base = {i: i for i in range(7)}
    treap = Treap(base)
    del treap[1]
    assert 1 not in treap
