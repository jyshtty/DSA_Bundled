"""
Problem: Coin Change
Link: https://leetcode.com/problems/coin-change/

Description:
    Given an array of coin denominations and an amount, return the fewest
    number of coins needed to make up the amount. Return -1 if impossible.

Examples:
    Input:  coins = [1,2,5], amount = 11    Output: 3  (5+5+1)
    Input:  coins = [2], amount = 3         Output: -1

Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 2^31 - 1
    0 <= amount <= 10^4
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # base case: 0 coins needed to make amount 0

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
