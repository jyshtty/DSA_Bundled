# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

#     Input: digits = "23"
#     Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]




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
