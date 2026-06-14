"""
Problem: House Robber II
Link: https://leetcode.com/problems/house-robber-ii/

Description:
    Houses are in a circle (first and last are adjacent). Return the
    maximum money you can rob without robbing adjacent houses.

Examples:
    Input:  nums = [2,3,2]      Output: 3
    Input:  nums = [1,2,3,1]    Output: 4

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev2, prev1 = 0, 0
            for h in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + h)
            return prev1

        # can't rob both first and last house — try both exclusions, take the max
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
