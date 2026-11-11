"""
Problem: Daily Temperatures
Link: https://leetcode.com/problems/daily-temperatures/

Description:
    Given an array of daily temperatures, return an array answer where
    answer[i] is the number of days you have to wait after day i for a
    warmer temperature. If no future warmer day exists, answer[i] = 0.

Examples:
    Input:  temperatures = [73,74,75,71,69,72,76,73]    Output: [1,1,4,2,1,1,0,0]
    Input:  temperatures = [30,40,50,60]                 Output: [1,1,1,0]

Constraints:
    1 <= temperatures.length <= 10^5
    30 <= temperatures[i] <= 100
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [len(temperatures) - 1]
        ans = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):

            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1] - i

            stack.append(i)

        return ans




