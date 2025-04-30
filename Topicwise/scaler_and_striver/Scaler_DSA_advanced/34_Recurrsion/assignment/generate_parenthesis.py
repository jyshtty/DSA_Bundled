class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, n):
        output_arr = []
        self.backtrack(output_arr, "", 0, 0, n)
        return output_arr


    def backtrack(self, output_arr, current_string, open, close, max):
        print(current_string)
        if len(current_string) == (max * 2):
            output_arr.append(current_string)
            return
        if(open < max):
            self.backtrack(output_arr, current_string + '(', open+1 ,close, max)
        if (close < open):
            self.backtrack(output_arr, current_string + ')', open, close+1, max)

if __name__ == "__main__":
    n = 3
    obj = Solution()
    print(obj.generateParenthesis(n))