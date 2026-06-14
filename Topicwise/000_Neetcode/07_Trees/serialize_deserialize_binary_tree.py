"""
Problem: Serialize and Deserialize Binary Tree
Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Description:
    Design an algorithm to serialize a binary tree to a string and
    deserialize that string back to the original tree.

Examples:
    Input:  [1,2,3,null,null,4,5]
    Serialize: "1,2,N,N,3,4,N,N,5,N,N"
    Deserialize: [1,2,3,null,null,4,5]

Constraints:
    0 <= number of nodes <= 10^4
    -1000 <= Node.val <= 1000
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")  # sentinel for null children
        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        tokens = deque(data.split(","))
        root = TreeNode(int(tokens.popleft()))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            left_val = tokens.popleft()
            right_val = tokens.popleft()
            if left_val != "N":
                node.left = TreeNode(int(left_val))
                queue.append(node.left)
            if right_val != "N":
                node.right = TreeNode(int(right_val))
                queue.append(node.right)
        return root
