"""
Problem: Subtree of Another Tree
Link: https://leetcode.com/problems/subtree-of-another-tree/

Description:
    Given the roots of two binary trees root and subRoot, return true if
    there is a subtree of root with the same structure and node values as subRoot.

Examples:
    Input:  root = [3,4,5,1,2], subRoot = [4,1,2]          Output: True
    Input:  root = [3,4,5,1,2,null,null,null,null,0],
            subRoot = [4,1,2]                               Output: False

Constraints:
    1 <= root nodes <= 2000
    1 <= subRoot nodes <= 1000
    -10^4 <= Node.val <= 10^4
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self._isSame(root, subRoot):
            return True
        # check both subtrees — the match could start at any node
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def _isSame(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self._isSame(p.left, q.left) and self._isSame(p.right, q.right)
