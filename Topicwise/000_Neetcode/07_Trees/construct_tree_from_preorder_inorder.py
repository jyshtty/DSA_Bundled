"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Description:
    Given two integer arrays preorder and inorder, construct and return
    the binary tree.

Examples:
    Input:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]

    Input:  preorder = [-1], inorder = [-1]
    Output: [-1]

Constraints:
    1 <= n <= 3000
    -3000 <= preorder[i], inorder[i] <= 3000
    Both arrays contain unique values and are valid traversals.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # index map for O(1) lookup of root position in inorder
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = inorder_index[root_val]  # elements left of mid are in left subtree
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)
