"""
Problem: Count Good Nodes in Binary Tree
Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Description:
    A node X is "good" if on the path from root to X there are no nodes
    with a value greater than X. Given the root, return the count of good nodes.

Examples:
    Input:  [3,1,4,3,null,1,5]    Output: 4
    Input:  [3,3,null,4,2]        Output: 3
    Input:  [1]                   Output: 1

Constraints:
    1 <= number of nodes <= 10^5
    -10^4 <= Node.val <= 10^4
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            is_good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)  # pass down the updated max to children
            return is_good + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, float('-inf'))
