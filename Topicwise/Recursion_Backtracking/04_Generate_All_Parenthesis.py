# Generate All Parenthesis
# # # Example: n = 3
# # # Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]    

class Solution:
    def generateParenthesis(self, n):
        stack = []
        left = right = n
        result = []
        self.generate(stack, left, right, result)
        return result

    def generate(self, stack, left, right, result):
        if left == 0 and right == 0:
            result.append("".join(stack))
            return
        if left != 0:
            stack.append("(")
            self.generate(stack, left - 1, right, result)
            stack.pop()
        if right < left:
            stack.append(")")
            self.generate(stack, left, right - 1, result)
            stack.pop()
