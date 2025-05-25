# 17. Letter Combinations of a Phone Numberfrom typing import List

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        hm = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        ans = []

        def generate(index, temp):
            if index == len(digits):
                ans.append(temp)
                return

            for ch in hm[digits[index]]:
                generate(index + 1, temp + ch)

        generate(0, "")
        return ans
