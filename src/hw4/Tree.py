class TreapNode:
    def __init__(self, key, priority):
        self.key = key
        self.left = None
        self.right = None
        self.priority = priority

    def __str__(self):
        return str(f"Key: {self.key}, priority:{self.priority}")


class Treap(TreapNode):

    def print(tree: TreapNode):
        if tree is None:
            return
        Treap.print(tree.left)
        print(tree)
        Treap.print(tree.right)

    def add_node(self, node):
        current = self
        if current.left is None | current.left.key > node.key:
            node.left = current.left
            node.right = current.right
            current.left

    @staticmethod
    def merge(first_tree: TreapNode, second_tree: TreapNode):
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


root = Treap(2, 2)
left = TreapNode(1, 1)
right = TreapNode(3, 3)
right
root.left = left
root.right = right
root.print()
