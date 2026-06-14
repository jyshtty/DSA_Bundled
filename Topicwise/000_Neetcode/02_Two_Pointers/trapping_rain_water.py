"""
Problem: Trapping Rain Water
Link: https://leetcode.com/problems/trapping-rain-water/

Description:
    Given n non-negative integers representing an elevation map where the
    width of each bar is 1, compute how much water it can trap after raining.

Examples:
    Input:  height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]    Output: 6
    Input:  height = [4, 2, 0, 3, 2, 5]                        Output: 9

Constraints:
    n == height.length
    1 <= n <= 2 * 10^4
    0 <= height[i] <= 10^5
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                # water at this cell is bounded by the shorter side (left_max)
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water
