class Node:
    def __init__(self, val= None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def search_recursive(self, root, target):
        if not root:
            return False
        if root.val == target:
            return True # because height of leaf is 0. But if we return 0 it will give us 1
        return self.search_recursive(root.left, target) or self.search_recursive(root.right, target)  # Short circuiting

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    obj = Solution()
    print(obj.search_recursive(root, 2))


