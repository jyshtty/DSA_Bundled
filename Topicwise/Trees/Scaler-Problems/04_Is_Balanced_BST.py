class Node:
    def __init__(self, val= None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    ans = 1

    def findDepth(self, node, depth):
        if node == None:
            return depth - 1
        lt_dt = self.findDepth(node.left, depth + 1)
        rt_dt = self.findDepth(node.right, depth + 1)
        if abs(lt_dt - rt_dt) > 1:
            self.ans = 0
        return max(lt_dt, rt_dt)

    def isBalanced(self, A):
        self.findDepth(A, 0)
        return self.ans

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    obj = Solution()
    print(obj.isBalanced(root, 2))