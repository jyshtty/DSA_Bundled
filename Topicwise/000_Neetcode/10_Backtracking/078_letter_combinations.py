"""
Problem: Letter Combinations of a Phone Number
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Description:
    Given a string of digits (2-9), return all possible letter combinations
    that the number could represent (like old phone keypads).

Examples:
    Input:  digits = "23"    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    Input:  digits = ""      Output: []
    Input:  digits = "2"     Output: ["a","b","c"]

Constraints:
    0 <= digits.length <= 4
    digits[i] is in ['2', '9'].
"""

from typing import List


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
