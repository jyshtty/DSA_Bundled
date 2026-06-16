"""
Problem: Combination Sum
Link: https://leetcode.com/problems/combination-sum/

Description:
    Given an array of distinct integers candidates and a target integer,
    return all unique combinations that sum to target. The same number may
    be used an unlimited number of times.

Examples:
    Input:  candidates = [2,3,6,7], target = 7    Output: [[2,2,3],[7]]
    Input:  candidates = [2,3,4], target = 6       Output: [[2,2,2],[2,4],[3,3]]

Constraints:
    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    All candidates are distinct.
    1 <= target <= 40
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])  # i not i+1 — reuse allowed
                current.pop()

        backtrack(0, [], target)
        return result
