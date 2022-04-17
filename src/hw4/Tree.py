import random
from dataclasses import dataclass
from typing import Any, Tuple, Optional


@dataclass
class TreapNode:
    """
    Treap Node data structure :)
    """

    def __init__(self, key, value):
        self.key: int = key
        self.priority: int = random.randint(0, 10e9)
        self.value: Any = value
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

    def __repr__(self):
        return f"Node: Key:{self.key}, Priority:{self.priority}, Value: {self.value}"


class Treap:
    """
    Tree + heap structure
    """

    def __init__(self, nodes: dict):
        self.root: Optional[TreapNode] = None
        for key in nodes:
            self.insert(TreapNode(key, nodes[key]))

    def __repr__(self):
        return str(self.root)

    def __iter__(self):
        for node in self.root:
            yield node.key

    def __contains__(self, item):
        return True if self.find(item) else False

    def __setitem__(self, key, value):
        self.insert(TreapNode(key, value))

    def __getitem__(self, item):
        find_result = self.find(item)
        if find_result is None:
            raise KeyError(f"key: {item} was not found in the treap")
        return find_result.value

    def __delitem__(self, key_to_remove):
        node = self.find(key_to_remove)
        if node is not None:
            left, right = split(self.root, key_to_remove)
            self.root = merge(left, right)

    def find(self, key: int):
        """
        Finds the value of the node with the given key
        """
        current_node = self.root
        while current_node is not None:
            if current_node.key == key:
                return current_node
            if current_node.key < key:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return None

    def clear(self):
        self.root = None

    def insert(self, node_to_insert):
        """
        Inserts new node to the tree
        """
        if self.root is None:
            self.root = node_to_insert
        else:
            left, right = split(self.root, node_to_insert.key)
            self.root = merge(merge(left, node_to_insert), right)


def split(node: TreapNode, division_key: int):
    """
    Splits a tree by given key
    """
    if node is None:
        return None, None
    if node.key < division_key:
        first_tree, second_tree = split(node.right, division_key)
        node.right = first_tree
        return node, second_tree
    else:
        first_tree, second_tree = split(node.left, division_key)
        node.left = first_tree
        return first_tree, node


def merge(first_tree, second_tree):
    """
    Merges two trees into one
    """
    if first_tree is None:
        return second_tree
    if second_tree is None:
        return first_tree
    if first_tree.priority > second_tree.priority:
        first_tree.right = merge(first_tree.right, second_tree)
        return first_tree
    else:
        second_tree.left = merge(first_tree, second_tree.left)
        return second_tree
