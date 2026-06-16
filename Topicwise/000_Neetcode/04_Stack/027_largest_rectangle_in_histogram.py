"""
Problem: Largest Rectangle in Histogram
Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

Description:
    Given an array of integers heights representing a histogram where each
    bar has width 1, return the area of the largest rectangle in the histogram.

Examples:
    Input:  heights = [2,1,5,6,2,3]    Output: 10
    Input:  heights = [2,4]            Output: 4

Constraints:
    1 <= heights.length <= 10^5
    0 <= heights[i] <= 10^4
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores (start_index, height); start_index is how far left we can extend
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            # pop taller bars — they can't extend past this shorter bar
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx  # this bar could have started as far left as the popped bar

            stack.append((start, h))

        # any remaining bars in the stack extend to the end of the histogram
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))

        return max_area
