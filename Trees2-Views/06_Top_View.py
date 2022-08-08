# Classic code - must see. Top View - Same as vertical view. But push only first element to hashmap
# Idea is put the first number with the distinct distance in hashmap. - Which gives you the top order. 

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
    def topView(self, A):
        curr = A
        q = deque()
        q.append([curr, 0])

        ans = []
        hashmap = {}

        while(q):
            node, distance = q.popleft()
            if distance not in hashmap:
                hashmap[distance] = [node.data]
                ans.append(node.data)

            if node.left:
                q.append([node.left, distance-1])
            if node.right:
                q.append([node.right, distance+1])

        return ans

# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

obj = Solution()
print(obj.topView(root))




