import copy


class TreapNode:
    def __init__(self, key, priority):
        self.key = key
        self.left = None
        self.right = None
        self.priority = priority

    def __str__(self):
        return str(f"Key: {self.key}, priority:{self.priority}")

    def print(self):
        if self is None:
            return
        TreapNode.print(self.left)
        print(self)
        TreapNode.print(self.right)


class Treap(TreapNode):
    def __init__(self: TreapNode, dictionary: dict):
        keys = list(dictionary.keys())
        self.root = TreapNode(keys[0], dictionary[keys[0]])
        for key in keys[1:]:
            self.root = Treap.insert(self.root, TreapNode(key, dictionary[key]))

    @staticmethod
    def merge(first_tree: TreapNode, second_tree: TreapNode) -> TreapNode:
        if first_tree is None:
            return second_tree
        if second_tree is None:
            return first_tree
        if first_tree.priority > second_tree.priority:
            first_tree.right = Treap.merge(first_tree.right, second_tree)
            return first_tree
        else:
            second_tree.left = Treap.merge(first_tree, second_tree.left)
            return second_tree

    @staticmethod
    def split(treap: TreapNode, division_key: int) -> (TreapNode, TreapNode):
        tree = copy.deepcopy(treap)
        if tree is None:
            return None, None
        if tree.key < division_key:
            first_tree, second_tree = Treap.split(tree.right, division_key)
            tree.right = first_tree
            return tree, second_tree
        else:
            first_tree, second_tree = Treap.split(tree.left, division_key)
            tree.left = first_tree
            return first_tree, tree

    @staticmethod
    def insert(treap: TreapNode, node: TreapNode) -> TreapNode:
        if treap is None:
            return node
        if node.priority > treap.priority:
            node.left, node.right = Treap.split(treap, node.key)
            return node
        if treap.key > node.key:
            treap.left = Treap.insert(treap.left, node)
            return treap
        else:
            treap.right = Treap.insert(treap.right, node)
            return treap


base = {i: i for i in range(7)}
root = Treap(base)
root.root.print()
