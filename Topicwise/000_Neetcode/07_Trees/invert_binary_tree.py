"""
Problem: Invert Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree/

Description:
    Given the root of a binary tree, invert the tree and return its root.

Examples:
    Input:  [4,2,7,1,3,6,9]    Output: [4,7,2,9,6,3,1]
    Input:  [2,1,3]            Output: [2,3,1]
    Input:  []                 Output: []

Constraints:
    0 <= number of nodes <= 100
    -100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
