class TreapNode:
    def __init__(self, key, priority):
        self.key = key
        self.left = None
        self.right = None
        self.priority = priority

    def __str__(self):
        return str(f"Key: {self.key}, priority:{self.priority}")


class Treap(TreapNode):

    def __str__(self):
        return str(f"Key: {self.key}, priority:{self.priority}")

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

root = Treap(2, 2)
left = TreapNode(1, 1)
right = TreapNode(3, 3)
right
root.left = left
root.right = right

root.print()