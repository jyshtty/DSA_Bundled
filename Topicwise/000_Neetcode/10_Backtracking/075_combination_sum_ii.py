"""
Problem: Combination Sum II
Link: https://leetcode.com/problems/combination-sum-ii/

Description:
    Given a collection of candidate numbers (may contain duplicates) and
    a target, return all unique combinations that sum to target. Each number
    may only be used once.

Examples:
    Input:  candidates = [10,1,2,7,6,1,5], target = 8
    Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Constraints:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # sorted array — no point continuing
                # skip duplicate candidates at the same level to avoid duplicate combos
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])  # i+1: each used once
                current.pop()

        backtrack(0, [], target)
        return result
