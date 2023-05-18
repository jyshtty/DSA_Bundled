class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return
        hm = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        res = []

        def generate(index, ans):
            if len(ans) == len(digits):
                res.append(ans)
                return
            for i in hm[int(digits[index])]:
                generate(index + 1, ans + i)

        generate(0, "")
        return res
