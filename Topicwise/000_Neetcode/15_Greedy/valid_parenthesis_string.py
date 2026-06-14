"""
Problem: Valid Parenthesis String
Link: https://leetcode.com/problems/valid-parenthesis-string/

Description:
    Given a string s containing '(', ')', and '*' (can be '(', ')', or ''),
    return true if the string is valid.

Examples:
    Input:  s = "()"        Output: True
    Input:  s = "(*)"       Output: True
    Input:  s = "(*))"      Output: True

Constraints:
    1 <= s.length <= 100
    s[i] is '(', ')', or '*'
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        # Track range of possible open-paren counts [lo, hi]
        # lo = minimum open parens possible (treat '*' as ')')
        # hi = maximum open parens possible (treat '*' as '(')
        lo = hi = 0

        for c in s:
            if c == '(':
                lo += 1; hi += 1
            elif c == ')':
                lo -= 1; hi -= 1
            else:  # '*'
                lo -= 1; hi += 1
            # hi < 0 means too many ')' even in the best case
            if hi < 0:
                return False
            # lo can't go below 0 — can't have negative open parens
            lo = max(lo, 0)

        return lo == 0
