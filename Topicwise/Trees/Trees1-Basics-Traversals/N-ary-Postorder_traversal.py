# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

# explanation:




class Solution:
    def postorder(self, root):
        if not root:
            return None
        stack = [root]
        ans = []

        while stack:
            temp = stack.pop()
            if temp:
                ans.append(temp.val)
                stack.extend(temp.children) # this is beautiful part. we are adding children as it is. so that when we pop we get rightmost child first.
        return ans[::-1]
        # finally we reverse the ans to get postorder
   