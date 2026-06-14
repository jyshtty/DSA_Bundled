"""
Problem: Binary Tree Right Side View
Link: https://leetcode.com/problems/binary-tree-right-side-view/

Description:
    Given the root of a binary tree, return the values of the nodes you
    can see standing on the right side, ordered from top to bottom.

Examples:
    Input:  [1,2,3,null,5,null,4]    Output: [1,3,4]
    Input:  [1,null,3]               Output: [1,3]
    Input:  []                       Output: []

Constraints:
    0 <= number of nodes <= 100
    -100 <= Node.val <= 100
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:  # last node at this level is the rightmost visible
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
