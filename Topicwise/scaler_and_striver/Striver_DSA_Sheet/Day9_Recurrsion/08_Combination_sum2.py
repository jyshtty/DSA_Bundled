# leetcode 40: Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
# https://leetcode.com/problems/combination-sum-ii/
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
# Approach: Backtracking with sorting
# Time Complexity: O(2^n)
# Space Complexity: O(n)
# Implementation:


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