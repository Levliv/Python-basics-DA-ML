from random import randint


def merge(first_tree, second_tree):
    """
    Merges 2 trees into 1.
    NB: it is important that keys in the first_tree should less than in the right one.
    """

    if first_tree is None:
        return second_tree
    if second_tree is None:
        return first_tree
    if first_tree.priority >= second_tree.priority:
        first_tree.right = merge(first_tree.right, second_tree)
        return first_tree
    else:
        second_tree.left = merge(first_tree, second_tree.left)
        return second_tree


def split(tree, key: int):
    """
    Splits the tree into 2 parts by the given key.
    """

    if tree is None:
        return None, None
    if key >= tree.key:
        a, b = split(tree.right, key)
        tree.right = a
        return tree, b
    else:
        a, b = split(tree.left, key)
        tree.left = b
        return a, tree


class Node:
    def __init__(self, key_passed: int, priority_passed: int, left_passed=None, right_passed=None):
        self.key: int = key_passed
        self.priority: int = priority_passed
        self.left: Node = left_passed
        self.right: Node = right_passed

    def __repr__(self):
        return (
            f"Node_id: {id(self)}, key: {self.key}, priority: {self.priority}\n left Node: {id(self.left)}\n  "
            f"right Node: {id(self.right)}"
        )

    def __eq__(self, other):
        return self.key == other.key and self.priority == other.priority

    def __iter__(self):
        """
        Прмой (Pre-order) обход
        """

        yield self
        if self.left is not None:
            yield from self.left
        if self.right is not None:
            yield from self.right


class Tree:
    root: Node = None

    def __init__(self, elements: map):
        self.tree_size: int = 0
        for key, priority in elements.items():
            n = Node(key, priority)
            self.add(n)

    def add(self, other: Node):
        self.tree_size += 1
        if self.root is None:
            self.root = other
        else:
            (a, b) = split(self.root, other.key)
            self.root = merge(merge(a, other), b)

    def delete(self, key: int):
        self.tree_size -= 1
        a, b = split(self.root, key)
        a1, a2 = split(a, key - 1)
        self.root = merge(a1, b)

    def find(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            if key > current.key:
                current = current.right
            else:
                current = current.left
        return None

    def __contains__(self, key):
        return self.find(key)

    def __getitem__(self, key):
        item = self.find(key)
        if item is not None:
            return item
        raise IndexError("Element with that key doesn't exist")

    def __setitem__(self, key, priority):
        self.add(Node(key, priority))

    def __delitem__(self, key):
        self.delete(key)

    def __iter__(self):
        """
        Прмой (Pre-order) обход
        """

        if self.root is not None:
            for node in self.root:
                yield node

    def __repr__(self):
        s = ""
        for node in self:
            s += str(node)
        return s
