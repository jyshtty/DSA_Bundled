# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightview(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque

        q = deque([root])
        res = []
        while q:
            size = len(q)
            ans = []
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                ans.append(node.val)
            res.append(ans[-1])
        return res