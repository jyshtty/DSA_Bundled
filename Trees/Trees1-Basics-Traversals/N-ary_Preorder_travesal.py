# when we do stack pop we pop from top of stack. so while inserting we insert[::-1]



class Solution:
    def preorder(self, root):
        if not root:
            return None

        stack = []
        ans = []
        stack.append(root)
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            stack.extend(temp.children[::-1])
        return ans
