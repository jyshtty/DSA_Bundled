def inordertraversal(root):
    if not root:
        return
    inordertraversal(root.left)
    print(root.data)
    inordertraversal(root.right)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key