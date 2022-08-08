class Solution:
    def generate_parenthesis(self, n):
        # only add open parenthesis if open < n
        # only add closing parenthesis if closed < open
        # valid if open == closed == n
        stack = []
        res = []
        def backtracking(open, closed):
            if open == closed == n:
                res.append("".join(stack))
            if open<n:
                stack.append("(")
                backtracking(open+1, closed)
                stack.pop()

            if closed<open:
                stack.append(")")
                backtracking(open, closed+1) # last time when execution of this line is done, stack will look like [( ( ( ) ) )], and when last time execution of this line is done it prints.  This line was called by bactracking (3, 2)
                stack.pop()

        backtracking(0, 0)
        return res

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
        if left != 0:
            self.generate(stack + ["("], left - 1, right, result)
        if right > left:
            self.generate(stack + [")"], left, right - 1, result)



