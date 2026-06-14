"""
Problem: Find Minimum in Rotated Sorted Array
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Description:
    Given a sorted array that has been rotated between 1 and n times,
    find the minimum element. Must run in O(log n).

Examples:
    Input:  nums = [3,4,5,1,2]      Output: 1
    Input:  nums = [4,5,6,7,0,1,2]  Output: 0
    Input:  nums = [11,13,15,17]     Output: 11

Constraints:
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All integers are unique.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                # mid is in the left (larger) portion; minimum is to the right
                left = mid + 1
            else:
                # mid is in the right (smaller) portion; minimum is at mid or to the left
                right = mid

        return nums[left]
