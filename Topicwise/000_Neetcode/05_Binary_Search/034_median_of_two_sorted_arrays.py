"""
Problem: Median of Two Sorted Arrays
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Description:
    Given two sorted arrays nums1 and nums2, return the median of the
    two sorted arrays combined. Must run in O(log(m+n)).

Examples:
    Input:  nums1 = [1,3], nums2 = [2]          Output: 2.0
    Input:  nums1 = [1,2], nums2 = [3,4]        Output: 2.5

Constraints:
    0 <= nums1.length, nums2.length <= 1000
    1 <= nums1.length + nums2.length <= 2000
    -10^6 <= nums1[i], nums2[i] <= 10^6
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # always binary search on the shorter array to minimize iterations
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n) // 2
        left, right = 0, m

        while left <= right:
            i = left + (right - left) // 2  # partition index for nums1
            j = half - i                    # partition index for nums2

            # values just left and right of each partition
            left1  = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i]     if i < m else float('inf')
            left2  = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j]     if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                # correct partition found
                if (m + n) % 2 == 1:
                    return float(min(right1, right2))
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1

        return 0.0
