"""
Problem: Validate Binary Search Tree
Link: https://leetcode.com/problems/validate-binary-search-tree/

Description:
    Given the root of a binary tree, determine if it is a valid BST.
    A valid BST: left subtree has only nodes < node.val,
    right subtree has only nodes > node.val, and both subtrees are BSTs.

Examples:
    Input:  [2,1,3]          Output: True
    Input:  [5,1,4,null,null,3,6]    Output: False  (4 in right subtree < root 5)

Constraints:
    1 <= number of nodes <= 10^4
    -2^31 <= Node.val <= 2^31 - 1
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lo, hi):
            if not node:
                return True
            if not (lo < node.val < hi):
                return False
            # tighten the valid range as we go deeper
            return validate(node.left, lo, node.val) and validate(node.right, node.val, hi)

        return validate(root, float('-inf'), float('inf'))
