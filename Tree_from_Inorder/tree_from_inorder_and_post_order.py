# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        def construct(left, right):
            if left > right:
                return None

            root_Value = postorder.pop()
            root_Node = TreeNode(root_Value)

            index = hm[root_Value]

            root_Node.right = construct(index + 1, right)
            root_Node.left = construct(left, index - 1)
            return root_Node

        hm = {val: idx for idx, val in enumerate(inorder)}
        return construct(0, len(inorder) - 1)