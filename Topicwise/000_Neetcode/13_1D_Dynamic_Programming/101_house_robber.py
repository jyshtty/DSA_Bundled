"""
Problem: House Robber
Link: https://leetcode.com/problems/house-robber/

Description:
    Given an array of non-negative integers representing house values,
    rob non-adjacent houses to maximize money stolen.

Examples:
    Input:  nums = [1,2,3,1]    Output: 4  (rob house 1 and 3)
    Input:  nums = [2,7,9,3,1]  Output: 12 (rob house 1, 3, 5)

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 400
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0

        for num in nums:
            # best at this house: either skip it (prev1) or rob it (prev2 + num)
            prev2, prev1 = prev1, max(prev1, prev2 + num)

        return prev1
