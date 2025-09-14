# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p:
            return False
        
        if not q:
            return False
        
        if p.val != q.val:
            return False
        
        if p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
 
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:

        def dfs(root, subroot):

            if not root and not subroot:
                return True

            if not root:
                return False
            
            if not subroot:
                return True
            
            if self.sameTree(root, subroot):
                return True
            
            return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)
        return dfs(root, subroot)
        