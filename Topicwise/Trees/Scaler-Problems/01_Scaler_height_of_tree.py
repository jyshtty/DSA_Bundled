# Height of a node - distance from node to furthest leaf or number of edges from node to furthest leaf.
# Height of a tree - height of root node
# Height of a tree - max(height of left sub tree, height of right sub tree) + 1


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
    def height_recursive(self, root):
        if not root:
            return -1 # because height of leaf is 0. But if we return 0 it will give us 1
        ls = self.height_recursive(root.left)
        rs = self.height_recursive(root.right)
        return max(ls, rs) + 1

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    obj = Solution()
    print(obj.size(root))


