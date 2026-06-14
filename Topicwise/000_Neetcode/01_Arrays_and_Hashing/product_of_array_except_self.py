"""
Problem: Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/

Description:
    Given an integer array nums, return an array answer such that
    answer[i] is equal to the product of all the elements of nums
    except nums[i]. Must run in O(n) without using the division operator.

Examples:
    Input:  nums = [1, 2, 3, 4]     Output: [24, 12, 8, 6]
    Input:  nums = [-1, 1, 0, -3, 3] Output: [0, 0, 9, 0, 0]

Constraints:
    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix fits in a 32-bit integer.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # first pass: result[i] holds product of everything to the LEFT of i
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # second pass: multiply in product of everything to the RIGHT of i
        # reusing result[] avoids allocating a separate suffix array
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
