# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p:
            return False
        
        if not q:
            return False
        
        if p.val != q.val:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

 if __name__ == "__main__":
    p = TreeNode(1, 
            TreeNode(2, TreeNode(4), TreeNode(5)), 
            TreeNode(3,TreeNode(6), TreeNode(7)))

    q = TreeNode(1, 
            TreeNode(2, TreeNode(4), TreeNode(5)), 
            TreeNode(3,TreeNode(6), TreeNode(7)))

    sol = Solution()
    print(sol.isSameTree(p, q))       
        