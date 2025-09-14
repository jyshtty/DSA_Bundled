from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, (left + right))

            return 1 + max(left, right)
        
        dfs(root)
        return res

if __name__ == "__main__":
    node = TreeNode(1, 
            TreeNode(2, TreeNode(4), TreeNode(5)), 
            TreeNode(3,TreeNode(6), TreeNode(7)))

    sol = Solution()
    print(sol.diameterOfBinaryTree(node))