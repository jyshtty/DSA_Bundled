def preordertraversal(root):
    if not root:
        return
    print(root.data)
    preordertraversal(root.left)
    preordertraversal(root.right)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
