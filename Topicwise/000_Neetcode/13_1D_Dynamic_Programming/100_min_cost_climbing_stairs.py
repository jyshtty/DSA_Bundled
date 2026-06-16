"""
Problem: Min Cost Climbing Stairs
Link: https://leetcode.com/problems/min-cost-climbing-stairs/

Description:
    Given an integer array cost where cost[i] is the cost of the i-th step,
    you can start from step 0 or 1, and at each step can climb 1 or 2 steps.
    Return the minimum cost to reach the top (beyond the last index).

Examples:
    Input:  cost = [10,15,20]    Output: 15
    Input:  cost = [1,100,1,1,1,100,1,1,100,1]     Output: 6

Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp[i] = min cost to reach step i (not counting cost[i] yet)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            # arrive at i either from i-1 (paying cost[i-1]) or i-2 (paying cost[i-2])
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]
