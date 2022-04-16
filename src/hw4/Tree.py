import random
from dataclasses import dataclass
from typing import Any, Optional, Tuple


@dataclass
class TreapNode:
    """
    Treap Node data structure :)
    """

    def __init__(self, key, value):
        self.key: int = key
        self.priority: int = random.randint(0, 100)
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
    Simple tree + heap struct
    """

    def __init__(self, nodes: dict):
        self.root: Optional[TreapNode] = None
        for key in nodes:
            self.insert(TreapNode(key, nodes[key]))

    def __setitem__(self, key, value):
        self.insert(TreapNode(key, value))

    def __getitem__(self, item):
        find_result = self.find(item)
        if find_result is None:
            raise KeyError(f"key: {item} was not found in the treap")
        return find_result

    def __delitem__(self, key):
        self.remove(key)

    def __contains__(self, item):
        return self.find(item) is not None

    def __str__(self):
        return str(self.root)

    def __iter__(self):
        for node in self.root:
            yield node.key

    def clear(self):
        self.root = None

    def insert(self, node_to_insert: TreapNode):
        """
        Appends a new node to the tree
        """
        if self.root is None:
            self.root = node_to_insert
        else:
            less, bigger, equals = split(self.root, node_to_insert.key)
            self.root = merge(merge(less, node_to_insert), bigger)

    def remove(self, key_to_remove) -> TreapNode:
        """
        Removes value from the tree
        """
        less, bigger, equals = split(self.root, key_to_remove)
        if equals is None:
            raise KeyError(f"Node with this key: {key_to_remove} does not exist in the Treap")
        self.root = merge(less, bigger)
        return equals

    def find(self, key) -> Optional[TreapNode]:
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


def split(node, division_key):
    """
    Splits a tree by key
    """
    if node is None:
        return None, None, None
    if node.key < division_key:
        temp_node = split(node.right, division_key)
        node.right = temp_node[0]
        return node, temp_node[1], temp_node[2]
    elif node.key == division_key:
        return node.left, node.right, node
    else:
        temp_node = split(node.left, division_key)
        node.left = temp_node[1]
        return temp_node[0], node, temp_node[2]


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
