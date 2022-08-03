def postordertraversal(root):
    if not root:
        return
    postordertraversal(root.left)
    postordertraversal(root.right)
    print(root.data)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


