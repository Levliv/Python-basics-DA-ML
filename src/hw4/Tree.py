import copy
from random import randint
from typing import Any


def get_rand_priority():
    return randint(1, int(10e9))


class TreapNode:
    key: int
    value: Any
    priority: int

    def __init__(self, key: int, priority: int, value: int):
        self.key = key
        self.priority = priority
        self.value = value
        self.left = None
        self.right = None

    def __iter__(self):
        if self.left is not None:
            for node in self.left:
                yield node
        yield self
        if self.right is not None:
            for node in self.right:
                yield node

    def __str__(self):
        return str(f"Key: {self.key}, priority:{self.priority}, value: {self.value}")

    def __contains__(self, desired_key: int):
        if self.find(desired_key) is not None:
            return True
        else:
            return False

    def __repr__(self):
        return TreapNode.__str__(self)

    def __del__(self):
        if self is None:
            pass
        elif self.left is not None:
            TreapNode.__del__(self.left)
        elif self.right is not None:
            TreapNode.__del__(self.right)

        self.value = None
        self.priority = None
        self.key = None

    def find(self, key: int):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif key < self.key:
            return TreapNode.find(self.left, key)
        else:
            return TreapNode.find(self.right, key)

    def print(self):
        if self is None:
            return
        TreapNode.print(self.left)
        print(self)
        TreapNode.print(self.right)

    @staticmethod
    def merge(first_tree, second_tree):
        if first_tree is None:
            return second_tree
        if second_tree is None:
            return first_tree
        if first_tree.priority > second_tree.priority:
            first_tree.right = TreapNode.merge(first_tree.right, second_tree)
            return first_tree
        else:
            second_tree.left = TreapNode.merge(first_tree, second_tree.left)
            return second_tree

    @staticmethod
    def insert(treap, node):
        if treap is None:
            return node
        if node.priority > treap.priority:
            node.left, node.right = TreapNode.split(treap, node.key)
            return node
        if treap.key > node.key:
            treap.left = TreapNode.insert(treap.left, node)
            return treap
        else:
            treap.right = TreapNode.insert(treap.right, node)
            return treap

    @staticmethod
    def split(treap, division_key: int):
        tree = copy.deepcopy(treap)
        if tree is None:
            return None, None
        if tree.key < division_key:
            first_tree, second_tree = TreapNode.split(tree.right, division_key)
            tree.right = first_tree
            return tree, second_tree
        else:
            first_tree, second_tree = TreapNode.split(tree.left, division_key)
            tree.left = first_tree
            return first_tree, tree


class Treap:
    root: TreapNode

    def __init__(self: TreapNode, dictionary: dict):
        if len(dictionary) == 0:
            raise TypeError("Treap must consist of at least 1 node")
        else:
            keys = list(dictionary.keys())
            self.root = TreapNode(keys[0], get_rand_priority(), dictionary[keys[0]])
            for key in keys[1:]:
                self.root = TreapNode.insert(self.root, TreapNode(key, get_rand_priority(), dictionary[key]))

    def __contains__(self, key: int):
        TreapNode.__contains__(self.root, key)

    def __iter__(self):
        if self.root is not None:
            return iter(self.root)
        else:
            return None

    def __getitem__(self, key: int):
        result = self.root.find(key)
        if result is None:
            raise TypeError(f"Node with key {key} wasn't found in the treap")
        else:
            return result.value

    def __setitem__(self, key: int, value):
        node = self.root.find(key)
        if node is None:
            self.root = self.insert(TreapNode(key, get_rand_priority(), value))
        else:
            node.value = value

    def __delitem__(self, key: int):
        node = self.root.find(key)
        if node is None:
            return None
        else:
            left, right = TreapNode.split(self.root, key)
            self.root = TreapNode.merge(left, right)
            return node

    def print(self):
        return TreapNode.print(self.root)


if __name__ == "__main__":
    base = {i: i for i in range(7)}
    treap = Treap(base)
    print(treap)