"""
Problem: Maximum Subarray
Link: https://leetcode.com/problems/maximum-subarray/

Description:
    Given an integer array nums, find the contiguous subarray with the
    largest sum and return its sum.

Examples:
    Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]    Output: 6  ([4,-1,2,1])
    Input:  nums = [1]                          Output: 1
    Input:  nums = [5,4,-1,7,8]                Output: 23

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        current = nums[0]

        for num in nums[1:]:
            # if current sum is negative, starting fresh is better than extending
            current = max(num, current + num)
            best = max(best, current)

        return best
