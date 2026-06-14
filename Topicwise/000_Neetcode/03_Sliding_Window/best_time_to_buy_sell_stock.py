"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Description:
    Given an array prices where prices[i] is the price of a stock on day i,
    return the maximum profit from one buy and one sell.
    Return 0 if no profit is possible.

Examples:
    Input:  prices = [7, 1, 5, 3, 6, 4]    Output: 5  (buy at 1, sell at 6)
    Input:  prices = [7, 6, 4, 3, 1]        Output: 0  (always decreasing)

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            # profit if we sell today at current price, having bought at the cheapest seen so far
            max_profit = max(max_profit, price - min_price)

        return max_profit
