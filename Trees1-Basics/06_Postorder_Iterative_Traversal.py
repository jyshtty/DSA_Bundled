# Python program to perform iterative preorder traversal

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorderApproach2(root):
    stack = []
    curr = root
    ans = []

    while stack or curr:

        if curr:
            ans.append(curr.data)
            stack.append(curr)
            curr = curr.right
        else:
            temp = stack.pop()
            curr = temp.left
    return ans[::-1]

# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

print(postorderApproach2(root))
# Approach 2


