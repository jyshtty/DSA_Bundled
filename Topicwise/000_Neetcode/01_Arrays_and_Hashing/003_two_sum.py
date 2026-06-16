"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Description:
    Given an array of integers nums and an integer target, return indices
    of the two numbers such that they add up to target. Each input has
    exactly one solution, and you may not use the same element twice.

Examples:
    Input:  nums = [2, 7, 11, 15], target = 9    Output: [0, 1]
    Input:  nums = [3, 2, 4],      target = 6    Output: [1, 2]
    Input:  nums = [3, 3],         target = 6    Output: [0, 1]

Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # maps value -> index so we can look up the complement in O(1)
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i  # store after check to avoid using the same index twice
        return []
