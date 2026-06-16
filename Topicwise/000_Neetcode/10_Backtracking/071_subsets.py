"""
Problem: Subsets
Link: https://leetcode.com/problems/subsets/

Description:
    Given an integer array nums of unique elements, return all possible subsets.
    The solution set must not contain duplicate subsets. Return in any order.

Examples:
    Input:  nums = [1,2,3]    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    Input:  nums = [0]        Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All nums are unique.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            result.append(current[:])  # snapshot the current subset

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()  # undo the choice before trying the next element

        backtrack(0, [])
        return result
