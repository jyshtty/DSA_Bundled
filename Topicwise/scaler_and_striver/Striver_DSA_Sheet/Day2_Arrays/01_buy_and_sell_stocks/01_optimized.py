# leetcode 121: Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Approach: Keep track of min price and max profit
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:


def foo(A):
    mini = A[0]
    max_profit = 0
    for i in range(1, len(A)):
        if A[i] < mini:
            mini = A[i]
        else:
            max_profit = max(max_profit, (A[i] - mini))
    return max_profit

A = [7,1,5,3,6,4]
print(foo(A))


