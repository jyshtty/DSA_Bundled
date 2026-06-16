"""
Problem: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

Description:
    Given a string s containing '(', ')', '{', '}', '[', ']', determine
    if the input string is valid. A string is valid if every open bracket
    is closed by the same type and in the correct order.

Examples:
    Input:  s = "()"        Output: True
    Input:  s = "()[]{}"    Output: True
    Input:  s = "(]"        Output: False

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in pairs:
                # closing bracket must match the most recent unmatched opening bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0  # unmatched opening brackets would remain
