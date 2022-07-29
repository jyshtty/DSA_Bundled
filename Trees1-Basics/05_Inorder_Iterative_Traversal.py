# A binary tree node

# Steps
# 1. Create a stack
# 2. Initilize curr = root
# 3. put all curr.left to stack till curr is null
# 4. when curr is null, pop from stack, print poped value,
# 5. initilize curr to popped values right

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    stack = []
    curr = root

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack.pop()
            print(temp.data)
            curr = temp.right


# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
inorder(root)