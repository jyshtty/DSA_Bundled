"""
Problem: Coin Change II
Link: https://leetcode.com/problems/coin-change-ii/

Description:
    Return the number of combinations that make up the given amount
    using the coin denominations (unlimited supply of each coin).

Examples:
    Input:  amount = 5, coins = [1,2,5]    Output: 4
    Input:  amount = 3, coins = [2]         Output: 0

Constraints:
    1 <= coins.length <= 300
    1 <= coins[i] <= 5000
    0 <= amount <= 5000
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # one way to make 0: use no coins

        for coin in coins:
            for a in range(coin, amount + 1):
                # processing each coin as an outer loop ensures each combination
                # is counted once (order doesn't matter — combinations, not permutations)
                dp[a] += dp[a - coin]

        return dp[amount]
