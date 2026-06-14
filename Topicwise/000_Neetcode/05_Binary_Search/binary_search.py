"""
Problem: Binary Search
Link: https://leetcode.com/problems/binary-search/

Description:
    Given a sorted array of distinct integers and a target value, return
    the index of target, or -1 if not found. Must run in O(log n).

Examples:
    Input:  nums = [-1,0,3,5,9,12], target = 9    Output: 4
    Input:  nums = [-1,0,3,5,9,12], target = 2    Output: -1

Constraints:
    1 <= nums.length <= 10^4
    -10^4 < nums[i], target < 10^4
    All integers in nums are unique and sorted in ascending order.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2  # avoids integer overflow vs (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
