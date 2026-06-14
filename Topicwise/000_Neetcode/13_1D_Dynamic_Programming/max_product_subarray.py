"""
Problem: Maximum Product Subarray
Link: https://leetcode.com/problems/maximum-product-subarray/

Description:
    Given an integer array nums, find a contiguous subarray with the
    largest product and return that product.

Examples:
    Input:  nums = [2,3,-2,4]    Output: 6
    Input:  nums = [-2,0,-1]     Output: 0

Constraints:
    1 <= nums.length <= 2 * 10^4
    -10 <= nums[i] <= 10
    The product fits in a 32-bit integer.
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # track both min and max because a large negative * negative = large positive
        cur_max = cur_min = result = nums[0]

        for n in nums[1:]:
            # multiplying by n can flip min/max, so compute all candidates first
            candidates = (n, cur_max * n, cur_min * n)
            cur_max = max(candidates)
            cur_min = min(candidates)
            result = max(result, cur_max)

        return result
