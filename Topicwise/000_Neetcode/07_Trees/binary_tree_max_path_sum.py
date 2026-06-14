"""
Problem: Binary Tree Maximum Path Sum
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Description:
    A path in a binary tree is a sequence of nodes where each pair of
    adjacent nodes has an edge. The path sum is the sum of node values.
    Return the maximum path sum (path need not pass through the root).

Examples:
    Input:  [1,2,3]              Output: 6   (2->1->3)
    Input:  [-10,9,20,null,null,15,7]   Output: 42  (15->20->7)

Constraints:
    1 <= number of nodes <= 3 * 10^4
    -1000 <= Node.val <= 1000
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            # clamp negative contributions to 0 — a negative branch worsens the path
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # candidate: path that passes through this node using both children
            self.max_sum = max(self.max_sum, node.val + left + right)

            # return only the better single branch (can't split when returning to parent)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
