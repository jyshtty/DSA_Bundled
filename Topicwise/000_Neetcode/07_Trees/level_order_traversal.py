"""
Problem: Binary Tree Level Order Traversal
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Description:
    Given the root of a binary tree, return the level order traversal of
    its nodes' values (i.e., from left to right, level by level).

Examples:
    Input:  [3,9,20,null,null,15,7]    Output: [[3],[9,20],[15,7]]
    Input:  [1]                        Output: [[1]]
    Input:  []                         Output: []

Constraints:
    0 <= number of nodes <= 2000
    -1000 <= Node.val <= 1000
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)  # snapshot of current level width before adding children
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result
