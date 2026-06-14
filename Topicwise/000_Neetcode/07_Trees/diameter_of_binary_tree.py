"""
Problem: Diameter of Binary Tree
Link: https://leetcode.com/problems/diameter-of-binary-tree/

Description:
    The diameter of a binary tree is the length of the longest path between
    any two nodes (in terms of edges). The path may or may not pass through
    the root. Return the diameter.

Examples:
    Input:  [1,2,3,4,5]    Output: 3  (path: 4->2->1->3 or 5->2->1->3)
    Input:  [1,2]          Output: 1

Constraints:
    1 <= number of nodes <= 10^4
    -100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            # path through this node spans left + right edges
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)  # return height for the parent to use

        depth(root)
        return self.diameter
