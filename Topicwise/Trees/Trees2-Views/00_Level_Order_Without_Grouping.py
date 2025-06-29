class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

from collections import deque
def level_order(root):

    if not root:
        return []


    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

print(level_order(root))

    
