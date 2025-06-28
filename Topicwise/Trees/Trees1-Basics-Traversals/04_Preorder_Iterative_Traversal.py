# Python program to perform iterative preorder traversal

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Approach 1
def iterativePreorder(root):
    # Base CAse
    if root is None:
        return
    # create an empty stack and push root to it
    nodeStack = []
    nodeStack.append(root)

    # Pop all items one by one. Do following for every popped item
    # a) print it
    # b) push its right child
    # c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while (len(nodeStack) > 0):

        # Pop the top item from stack and print it
        node = nodeStack.pop()
        print(node.data, end=" ")

        # Push right and left children of the popped node
        # to stack
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)


# Idea is stack.pop always gives previous node when the curr.left is none.
def preorderApproach2(root):
    stack = []
    curr = root
    ans = []

    while stack or curr:

        if curr:
            ans.append(curr.data)
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack.pop()
            curr = temp.right
    return ans

# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
iterativePreorder(root)
print("")
print("Approach2")

print(preorderApproach2(root))
# Approach 2


