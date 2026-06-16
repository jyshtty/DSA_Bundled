"""
Problem: Lowest Common Ancestor of a BST
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Description:
    Given a BST and two nodes p and q, find their lowest common ancestor
    (the deepest node that is an ancestor of both p and q).

Examples:
    Input:  root = [6,2,8,0,4,7,9], p = 2, q = 8    Output: 6
    Input:  root = [6,2,8,0,4,7,9], p = 2, q = 4    Output: 2

Constraints:
    2 <= number of nodes <= 10^5
    -10^9 <= Node.val <= 10^9
    All Node.val are unique.
    p != q, both exist in the BST.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left   # both nodes are in the left subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right  # both nodes are in the right subtree
            else:
                return curr        # they split here — current node is the LCA
        return curr
