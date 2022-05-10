from random import randint
from typing import Any


class Node:
    """
    Узел дерева.
    """

    def __init__(self, key_passed: Any, priority_passed: Any, left_passed=None, right_passed=None):
        self.key: int = key_passed
        self.priority: int = priority_passed
        self.left: Node = left_passed
        self.right: Node = right_passed

    def __repr__(self):
        """
        Строковое представление узла.
        """
        return (
            f"Node_id: {id(self)}, key: {self.key}, priority: {self.priority}\n left Node: {id(self.left)}\n  "
            f"right Node: {id(self.right)}"
        )

    def __eq__(self, other):
        """
        Проверка двух узлов на равенство.
        """
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
    """
    Декартово дерево.
    """

    root: Node = None

    def __init__(self, elements: map):
        """
        Инициализация дерева при помощи массива, содержащего пары ключ: приоритет.
        """
        self.tree_size: int = 0
        for key, priority in elements.items():
            n = Node(key, priority)
            self.add(n)

    def add(self, other: Node):
        """
        Добавление нового узла в дерево.
        """
        self.tree_size += 1
        if self.root is None:
            self.root = other
        else:
            (a, b) = split(self.root, other.key)
            self.root = merge(merge(a, other), b)

    def delete(self, key: Any):
        """
        Удаление узла с заданным значением ключа.
        """
        self.tree_size -= 1
        a, b = split(self.root, key)
        a1, a2 = split(a, key - 1)
        self.root = merge(a1, b)

    def find(self, key: Any):
        """
        Поиск в дереве узла с заданным значением ключа.
        """
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            if key > current.key:
                current = current.right
            else:
                current = current.left
        return None

    def __contains__(self, key: Any):
        return self.find(key)

    def __getitem__(self, key: Any):
        """
        Получение узла дерева по ключу.
        """
        item = self.find(key)
        if item is not None:
            return item
        raise IndexError("Element with that key doesn't exist")

    def __setitem__(self, key: Any, priority: Any):
        """ """
        self.add(Node(key, priority))

    def __delitem__(self, key: Any):
        """
        Уделение произваольного элемента дерева по ключу.
        """
        self.delete(key)

    def __iter__(self):
        """
        Прмой (Pre-order) обход
        """

        if self.root is not None:
            for node in self.root:
                yield node

    def __repr__(self):
        """
        Строкое представление дерева.
        """
        s = ""
        for node in self:
            s += str(node)
        return s


def merge(first_tree: Tree, second_tree: Tree):
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


def split(tree: Tree, key: int):
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
