# Size - return the count of nodes.
#
# Idea - size of tree = size of left subtree + size of right subtree + 1

# Idea is of post order
#       First - calculate height of left sub tree
#       Second - calculate height of right sub tree
#       Third - At last the root.

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive
    def size(self, root):
        if not root:
            return 0
        ls = self.size(root.left)
        rs = self.size(root.right)
        return ls + rs + 1

    # Iterative
    def count(self, A):
        count = 0
        queue = []
        queue.append(A)
        while (len(queue) > 0):
            node = queue.pop(0)
            count = count + 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return count

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    obj = Solution()
    print(obj.size(root))
