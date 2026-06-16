"""
Problem: Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Description:
    Given the root of a binary tree, return its maximum depth (the number
    of nodes along the longest path from root to a leaf).

Examples:
    Input:  [3,9,20,null,null,15,7]    Output: 3
    Input:  [1,null,2]                 Output: 2

Constraints:
    0 <= number of nodes <= 10^4
    -100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # depth is 1 (current node) + the deeper of the two subtrees
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
