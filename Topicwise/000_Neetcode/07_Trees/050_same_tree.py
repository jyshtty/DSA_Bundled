"""
Problem: Same Tree
Link: https://leetcode.com/problems/same-tree/

Description:
    Given the roots of two binary trees, check if they are the same
    (structurally identical with the same node values).

Examples:
    Input:  p = [1,2,3], q = [1,2,3]        Output: True
    Input:  p = [1,2],   q = [1,null,2]     Output: False
    Input:  p = [1,2,1], q = [1,1,2]        Output: False

Constraints:
    0 <= number of nodes <= 100
    -10^4 <= Node.val <= 10^4
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
