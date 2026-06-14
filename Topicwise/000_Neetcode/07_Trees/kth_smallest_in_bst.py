"""
Problem: Kth Smallest Element in a BST
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Description:
    Given the root of a BST and an integer k, return the kth smallest
    value (1-indexed) of all the values of the nodes in the tree.

Examples:
    Input:  root = [3,1,4,null,2], k = 1    Output: 1
    Input:  root = [5,3,6,2,4,null,null,1], k = 3    Output: 3

Constraints:
    1 <= k <= n <= 10^4
    0 <= Node.val <= 10^4
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative inorder traversal yields BST values in sorted order
        stack = []
        curr = root
        count = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left   # go as far left as possible first

            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val

            curr = curr.right  # move to right subtree after visiting this node

        return -1
