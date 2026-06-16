"""
Problem: Single Number
Link: https://leetcode.com/problems/single-number/

Description:
    Given a non-empty array where every element appears twice except one,
    find the element that appears only once. Must use O(1) space.

Examples:
    Input:  nums = [2,2,1]          Output: 1
    Input:  nums = [4,1,2,1,2]      Output: 4

Constraints:
    1 <= nums.length <= 3 * 10^4
    -3 * 10^4 <= nums[i] <= 3 * 10^4
    Exactly one element appears once.
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR cancels out pairs: a ^ a = 0, a ^ 0 = a
        return result
