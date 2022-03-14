class Tree:
    def __init__(self, key, priority):
        self.key = key
        self.left = None
        self.right = None
        self.priority = priority

    def __str__(self):
        return str(f"Key: {self.key}, priority:{self.priority}")

    def print(self):
        if self.left is not None:
            print(self.left)

        print(self)

        if self.right is not None:
            print(self.right)

    def add_node(self, node):
        current = self
        if current.left is None | current.left.key > node.key:
            node.left = current.left
            node.right = current.right
            current.left

root = Tree(2, 2)
left = Tree(1, 1)
right = Tree(3, 3)
right
root.left = left
root.right = right

root.print()