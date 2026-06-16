"""
Problem: Generate Parentheses
Link: https://leetcode.com/problems/generate-parentheses/

Description:
    Given n pairs of parentheses, generate all combinations of
    well-formed parentheses.

Examples:
    Input:  n = 3    Output: ["((()))","(()())","(())()","()(())","()()()"]
    Input:  n = 1    Output: ["()"]

Constraints:
    1 <= n <= 8
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            if len(current) == 2 * n:
                result.append(current)
                return
            # can add '(' as long as we haven't used all n open brackets
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            # can add ')' only if there's an unmatched '(' to close
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack('', 0, 0)
        return result
