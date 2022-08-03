# Vertical View - All the nodes with same distance should come in same list.
#  maintain hashmap -
#                   key - distance
#                   value - list of nodes
#  only level order will work
# note - preorder, post order, inorder  will fail. We will not get data in the correct order

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
    def verticalOrder(self, A):
        curr = A
        q = deque()
        q.append([curr, 0])

        ans = []
        hashmap = {}

        mini = maxi = 0

        while(q):
            node, distance = q.popleft()
            mini = min(mini, distance)
            maxi = max(maxi, distance)

            if distance not in hashmap:
                hashmap[distance] = [node.data]
            else:
                hashmap[distance].append(node.data)

            if node.left:
                q.append([node.left, distance-1])
            if node.right:
                q.append([node.right, distance+1])

        ans = []
        for i in range(mini, maxi+1):
            ans.append(hashmap[i])

        return ans



# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

obj = Solution()
print(obj.verticalOrder(root))




