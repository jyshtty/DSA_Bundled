class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        q = []
        curr = A
        q.append(curr)
        maxi = 0

        while q:
            node = q.pop()
            maxi = max(maxi, node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return maxi

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    obj = Solution()
    print(obj.solve(root))