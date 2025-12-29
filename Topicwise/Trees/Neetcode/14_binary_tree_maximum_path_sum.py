

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
            

        res = float("-inf")
        def solve(root):
            nonlocal res

            if not root:
                return 0
            
            left_path_max_sum = max(0, solve(root.left))
            right_path_max_sum = max(0, solve(root.right))

            res = max(res, left_path_max_sum + right_path_max_sum + root.val)
            return root.val + max(left_path_max_sum, right_path_max_sum)

        solve(root)
        return res
        
