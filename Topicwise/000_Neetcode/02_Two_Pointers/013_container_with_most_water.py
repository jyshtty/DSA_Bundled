"""
Problem: Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/

Description:
    Given n non-negative integers height[i] representing vertical lines,
    find two lines that together with the x-axis form a container that
    holds the most water. Return the maximum amount of water.

Examples:
    Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]    Output: 49
    Input:  height = [1, 1]                           Output: 1

Constraints:
    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            water = width * min(height[left], height[right])
            max_water = max(max_water, water)

            # move the shorter line inward — moving the taller one can only decrease area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
