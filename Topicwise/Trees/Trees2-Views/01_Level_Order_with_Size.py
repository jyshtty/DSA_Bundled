# BFS using len of quque for find number of levels.
# O/p is list of liests


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
    def levelOrder(self, A):
        queue = deque()
        output = []
        if A:
            queue.append(A)
        while queue:
            size = len(queue)
            curr = [] # stores nodes data at current level
            for i in range(size):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                curr.append(temp.data)
            output.append(curr)
            # print(output)
        return output

# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

obj = Solution()
print(obj.levelOrder(root))
