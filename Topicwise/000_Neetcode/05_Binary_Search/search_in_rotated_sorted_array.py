"""
Problem: Search in Rotated Sorted Array
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

Description:
    Given a rotated sorted array of distinct integers and a target, return
    the index of target, or -1 if not found. Must run in O(log n).

Examples:
    Input:  nums = [4,5,6,7,0,1,2], target = 0    Output: 4
    Input:  nums = [4,5,6,7,0,1,2], target = 3    Output: -1

Constraints:
    1 <= nums.length <= 5000
    -10^4 <= nums[i], target <= 10^4
    All values are unique.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # determine which half is sorted
            if nums[left] <= nums[mid]:  # left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
