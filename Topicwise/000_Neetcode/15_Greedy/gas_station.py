"""
Problem: Gas Station
Link: https://leetcode.com/problems/gas-station/

Description:
    Given gas[i] and cost[i] for each station in a circular route, find
    the starting station index so you can complete the circuit. Return -1
    if impossible. The answer is guaranteed to be unique.

Examples:
    Input:  gas = [1,2,3,4,5], cost = [3,4,5,1,2]    Output: 3
    Input:  gas = [2,3,4], cost = [3,4,3]             Output: -1

Constraints:
    n == gas.length == cost.length
    1 <= n <= 10^5
    0 <= gas[i], cost[i] <= 10^4
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1  # total gas insufficient — no solution exists

        tank = 0
        start = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                # can't reach station i+1 from start — reset and try i+1 as new start
                tank = 0
                start = i + 1

        return start
