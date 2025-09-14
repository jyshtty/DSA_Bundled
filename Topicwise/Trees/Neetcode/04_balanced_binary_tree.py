from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            current_height = 1 + max(left_height, right_height)

            return [current_balanced, current_height]

        return dfs(root)[0]


if __name__ == "__main__":
    node = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    sol = Solution()
    print(sol.isBalanced(node))  # ✅ True
