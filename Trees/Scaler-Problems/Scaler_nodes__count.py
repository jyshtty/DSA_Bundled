# Definition for a  binary tree node
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Approach1 - Preorder
    def solve(self, root):
        stack = []
        curr = root
        count = 0

        while stack or curr:
            if curr:
                stack.append(curr)
                count += 1
                curr = curr.left
            else:
                temp = stack.pop()
                curr = temp.right
        return count


    # Approach2 -
    def solve1(self, A):
        count = 0
        queue = []
        queue.append(A)
        while (len(queue) > 0):
            node = queue.pop(0)
            count = count + 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return count

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    obj = Solution()
    print(obj.solve(root))
    print(obj.solve1(root))
