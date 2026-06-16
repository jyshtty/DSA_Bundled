"""
Problem: Best Time to Buy and Sell Stock with Cooldown
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Description:
    Given prices, find max profit with cooldown: after selling on day i,
    you cannot buy on day i+1 (must wait one day).

Examples:
    Input:  prices = [1,2,3,0,2]    Output: 3
    Input:  prices = [1]            Output: 0

Constraints:
    1 <= prices.length <= 5000
    0 <= prices[i] <= 1000
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # States: holding a stock, not holding (can buy), cooldown
        # hold[i] = max profit while holding stock on day i
        # free[i] = max profit while NOT holding and not in cooldown
        # cool[i] = max profit on cooldown (just sold)

        hold = -prices[0]
        free = 0
        cool = 0

        for price in prices[1:]:
            prev_hold, prev_free, prev_cool = hold, free, cool
            hold = max(prev_hold, prev_free - price)  # keep holding or buy (can only buy from free state)
            cool = prev_hold + price                  # sell today -> enter cooldown tomorrow
            free = max(prev_free, prev_cool)          # stay free or come off cooldown

        return max(free, cool)
