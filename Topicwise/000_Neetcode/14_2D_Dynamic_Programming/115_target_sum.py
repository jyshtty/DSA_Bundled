"""
Problem: Target Sum
Link: https://leetcode.com/problems/target-sum/

Description:
    Given an array of integers and a target, assign + or - to each integer.
    Return the number of ways to reach the target sum.

Examples:
    Input:  nums = [1,1,1,1,1], target = 3    Output: 5
    Input:  nums = [1], target = 1            Output: 1

Constraints:
    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    -1000 <= target <= 1000
"""

from typing import List
from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1  # one way to reach sum 0 before processing any number

        for num in nums:
            next_dp = defaultdict(int)
            for s, count in dp.items():
                next_dp[s + num] += count  # assign +
                next_dp[s - num] += count  # assign -
            dp = next_dp

        return dp[target]
