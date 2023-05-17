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
                stack.extend(temp.children)
        return ans[::-1]