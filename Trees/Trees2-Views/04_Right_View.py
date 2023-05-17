# Right View - 1st node of Level order of every level.
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def rightOrder(self, A):
        curr = A
        q = deque()
        q.append(curr)

        ans = []

        while(q):
            size = len(q)
            level = []
            for i in range(size):
                u = q.popleft()
                level.append(u.data)
                if u.left:
                    q.append(u.left)
                if u.right:
                    q.append(u.right)
            ans.append(level[-1])
        return ans

# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

obj = Solution()
print(obj.rightOrder(root))

# Approach2
# push level order right to left

# Approach3
# use stack instad of q


