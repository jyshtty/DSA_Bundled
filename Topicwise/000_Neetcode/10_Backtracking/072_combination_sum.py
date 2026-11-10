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

class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def backtrack(index, sum, temp):
            if index == len(candidates) or sum > target:
                return
            if sum == target:
                ans.append(temp.copy())
                return
            temp.append(candidates[index])
            backtrack(index, sum + candidates[index], temp)
            temp.pop()
            backtrack(index + 1, sum, temp)

        backtrack(0, 0, [])
        return ans
