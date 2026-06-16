"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Description:
    Given an integer array nums, return true if any value appears at least
    twice in the array, and return false if every element is distinct.

Examples:
    Input:  nums = [1, 2, 3, 1]             Output: True
    Input:  nums = [1, 2, 3, 4]             Output: False
    Input:  nums = [1, 1, 1, 3, 3, 4, 3]   Output: True

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # set gives O(1) avg lookup; a list would be O(n) per check
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
