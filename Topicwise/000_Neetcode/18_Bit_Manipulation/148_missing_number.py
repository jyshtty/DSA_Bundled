"""
Problem: Missing Number
Link: https://leetcode.com/problems/missing-number/

Description:
    Given an array containing n distinct numbers in range [0, n], return
    the missing number.

Examples:
    Input:  nums = [3,0,1]      Output: 2
    Input:  nums = [0,1]        Output: 2
    Input:  nums = [9,6,4,2,3,5,7,0,1]    Output: 8

Constraints:
    n == nums.length
    1 <= n <= 10^4
    0 <= nums[i] <= n
    All nums are distinct.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR all indices and values: pairs cancel out, leaving the missing index
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result
