"""
Problem: Burst Balloons
Link: https://leetcode.com/problems/burst-balloons/

Description:
    Given n balloons with values, burst all balloons to maximize coins.
    Bursting balloon i gives nums[left] * nums[i] * nums[right] coins
    where left and right are the adjacent non-burst balloons.

Examples:
    Input:  nums = [3,1,5,8]    Output: 167  ([3,5,8] -> [3,8] -> [8] -> [])
    Input:  nums = [1,5]        Output: 10

Constraints:
    1 <= nums.length <= 300
    0 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # add 1-value boundaries so edge balloons always have neighbors
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    # treat k as the LAST balloon to burst in the open interval (left, right)
                    # — this avoids having to track what's adjacent at burst time
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right]
                    )

        return dp[0][n - 1]
