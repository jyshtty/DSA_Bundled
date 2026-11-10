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

# Make sure you check target == sum before you check index == len(candidates)

class Solution:
    def combinationSum2(self, candidates, target):
        ans = []
        candidates.sort()

        def backtrack(index, sum, temp):
            if sum == target:
                ans.append(temp.copy())
                return

            if index == len(candidates) or sum > target:
                return

            temp.append(candidates[index])
            backtrack(index + 1, sum + candidates[index], temp)
            temp.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, sum, temp)

        backtrack(0, 0, [])
        return ans
