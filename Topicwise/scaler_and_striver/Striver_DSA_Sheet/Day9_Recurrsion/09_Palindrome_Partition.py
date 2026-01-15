# leetcode 131: Palindrome Partitioning
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# https://leetcode.com/problems/palindrome-partitioning/
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Approach: Backtracking
# Time Complexity: O(2^n)
# Space Complexity: O(n)
# Implementation:


class Solution:
    def isPalin(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

    def partition(self, s):
        ans = []
        curr = []
        def backtracking(i):
            if i == len(s):
                ans.append(curr.copy())
                return
            for j in range(i, len(s)):
                if self.isPalin(i, j, s):
                    curr.append(s[i: j + 1])
                    backtracking(j + 1)
                    curr.pop()
        backtracking(0)
        return ans


# https://www.starlux-airlines.com/{{locale|language_from_locale|lower|default("zh")}}-{{locale|country_from_locale|default("TW")}}
# /booking_code/{{affiliate_name}}?
#
# https://www.starlux-airlines.com/zh-TW/booking/skyscanner?ondCityCode%5B0%5D.origin=TPE&ondCityCode%5B0%5D.destination=PEN&ondCityCode%5B0%5D.month=08%2F2022&ondCityCode%5B0%5D.day=20&cabinClassCode=Y&numAdults=1&numChildren=0&numInfant=0&abcd&tripType=O&tansel=VjJ8Slg3MjEsWTFUV1NFQXw0NjYuNzB8VVNEfDA5NjI1MEVERUFGRDRFNEU4REEyMTkyREEyOEIxMzdFfEpY&hid=eyJpZCI6Im1NdlpkZ0c5S3pvUXJuZkRmMU9mcDdvMDJIV2tVVyIsIm8iOiIzODgifQ%3A1oLg5C%3A1hQRaEHTBjFiqGUWag9Rtv1pwNoXrJm7Nb31b91vUGs
# https://www.starlux-airlines.com/zh-TW/booking_code/Skyscanner?ondCityCode%5B0%5D.origin=TPE&ondCityCode%5B0%5D.destination=PEN&ondCityCode%5B0%5D.month=08%2F2022&ondCityCode%5B0%5D.day=20&cabinClassCode=Y&numAdults=1&numChildren=0&numInfant=0&abcd&tripType=O&tansel=VjJ8Slg3MjEsWTJUV1NFQXw0MTEuNzB8VVNEfDNDMjBCQzM5NjBFOTQ3MUY5QkRBQkVFRTkyRTZEMTc1fEpY&hid=eyJpZCI6Ik5HRlJSd1R0ZGdnZmVldTJBSDI3MTZvcE03MUd2NCIsIm8iOiIzODgifQ%3A1oLg4I%3AUMo-sVjIG864H6Cqs6rcDKaK4FqzK7hcGSUyFp5qCGc
# https://www.starlux-airlines.com/zh-TW/en-/booking/Skyscanner?ondCityCode%5B0%5D.origin=TPE&ondCityCode%5B0%5D.destination=PEN&ondCityCode%5B0%5D.month=08%2F2022&ondCityCode%5B0%5D.day=20&cabinClassCode=Y&numAdults=1&numChildren=0&numInfant=0&abcd&tripType=O&tansel=VjJ8Slg3MjEsWTFUV1NFQXw0NjYuNzB8VVNEfDg4RDE1MjVDODk2MTRFRDE5NkY5MkExRkUyRjA4NEQzfEpY&hid=eyJpZCI6ImlHMUI4MzBhOWlwWVBQd1VBNzByUTI1RzhNeTNpayIsIm8iOiIzODgifQ%3A1oLg72%3Ag0vnukr_ZA4vnaPJuxgCIJJ-JMXtV_CGFm5CJHFGjC8