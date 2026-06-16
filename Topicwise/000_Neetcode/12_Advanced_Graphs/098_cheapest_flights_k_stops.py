"""
Problem: Cheapest Flights Within K Stops
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/

Description:
    Given n cities and flights with prices, find the cheapest price from
    src to dst with at most k stops. Return -1 if no route.

Examples:
    Input:  n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
            src=0, dst=3, k=1    Output: 700

Constraints:
    1 <= n <= 100
    0 <= flights.length <= (n*(n-1)/2)
    0 <= k < n
"""

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford with at most k+1 edges
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices[:]  # use a copy so current round's updates don't affect each other
            for u, v, w in flights:
                if prices[u] != float('inf') and prices[u] + w < temp[v]:
                    temp[v] = prices[u] + w
            prices = temp

        return prices[dst] if prices[dst] != float('inf') else -1
