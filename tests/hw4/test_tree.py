import pytest
from src.hw4.Tree import Tree, Node, split, merge


def test_building():
    t = Tree({8: 1, 5: 2, 2: 15})
    res = t.root
    assert res == Node(2, 15)
    assert res.right == Node(5, 2)
    assert res.right.right == Node(8, 1)


def test_merge():
    t1 = Tree({1: 3, 2: 5, 4: 8, 6: 12})
    t2 = Tree({8: 22, 12: 5, 10: 15})
    res = merge(t1.root, t2.root)
    print(res)
    assert res == Node(8, 22)
    assert res.right == Node(10, 15)
    assert res.right.right == Node(12, 5)
    assert res.left == Node(6, 12)
    assert res.left.left == Node(4, 8)
    assert res.left.left.left == Node(2, 5)
    assert res.left.left.left.left == Node(1, 3)


def test_split():
    tree = Tree({1: 3, 2: 5, 4: 8, 6: 12, 8: 22, 12: 5, 10: 15})
    t1, t2 = split(tree.root, 6)
    print(t1)
    print(t2)
    assert t1 == Node(6, 12)
    assert t1.left == Node(4, 8)
    assert t1.left.left == Node(2, 5)
    assert t1.left.left.left == Node(1, 3)
    assert t2 == Node(8, 22)
    assert t2.right == Node(10, 15)
    assert t2.right.right == Node(12, 5)


def test_add():
    t1 = Tree({1: 3, 2: 5, 8: 8, 6: 12})
    t1.add(Node(3, 4))
    res = t1.root
    assert res == Node(6, 12)
    assert res.left == Node(2, 5)
    assert res.left.left == Node(1, 3)
    assert res.left.right == Node(3, 4)
    assert res.right == Node(8, 8)


def test_delete():
    t1 = Tree({1: 3, 2: 5, 8: 8, 6: 12})
    t1.delete(2)
    res = t1.root
    print(res)
    assert res == Node(6, 12)
    assert res.left == Node(1, 3)
    assert res.right == Node(8, 8)


def test_delete_border_case():
    t1 = Tree({1: 3, 2: 5, 8: 8, 6: 12})
    t1.delete(1)
    t1.delete(8)
    assert t1.root == Node(6, 12)
    assert t1.root.left == Node(2, 5)


def test_find():
    t1 = Tree({1: 3, 2: 5, 8: 8, 6: 12})
    assert t1.find(1) == Node(1, 3)
    assert t1.find(2) == Node(2, 5)
    assert t1.find(6) == Node(6, 12)
    assert t1.find(8) == Node(8, 8)


def test_find_key_not_found():
    t1 = Tree({1: 3, 2: 5, 8: 8, 6: 12})
    assert t1.find(5) is None
    assert t1.find(10) is None


def test_contains():
    t1 = Tree({1: 3, 2: 5, 8: 8, 6: 12})
    assert 2 in t1
    assert 1 in t1
    assert 6 in t1
    assert 8 in t1
    assert 7 not in t1


def test_get_element():
    t1 = Tree({1: 3, 2: 5, 8: 8, 6: 12})
    assert t1[2] == Node(2, 5)
    with pytest.raises(IndexError, match=r"exist") as e:
        t1[23]


def test_set_element():
    t1 = Tree({1: 3, 2: 5, 8: 8, 6: 12})
    t1[7] = 12
    assert t1[7] == Node(7, 12)
    assert t1[2] == Node(2, 5)


def test_del_element():
    t1 = Tree({1: 3, 2: 5, 8: 8, 6: 12})
    del t1[2]
    del t1[8]
    assert 2 not in t1
    assert 1 in t1
    assert 8 not in t1
    assert 6 in t1


def test_iter():
    t1 = Tree({1: 3, 2: 5, 8: 8, 6: 12})
    nodes = []
    for t in t1:
        nodes.append(t)
    assert nodes == [Node(6, 12), Node(2, 5), Node(1, 3), Node(8, 8)]
