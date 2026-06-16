"""
Problem: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/

Description:
    A phrase is a palindrome if, after converting all uppercase letters to
    lowercase and removing all non-alphanumeric characters, it reads the
    same forward and backward.
    Given a string s, return true if it is a palindrome, false otherwise.

Examples:
    Input:  s = "A man, a plan, a canal: Panama"   Output: True
    Input:  s = "race a car"                        Output: False
    Input:  s = " "                                 Output: True

Constraints:
    1 <= s.length <= 2 * 10^5
    s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # skip non-alphanumeric characters from both ends
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
