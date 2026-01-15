# leetcode 17: Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Approach: Backtracking
# Time Complexity: O(3^n * 4^m) where n is number of digits with 3 letters, m with 4
# Space Complexity: O(3^n * 4^m)
# Implementation:


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
