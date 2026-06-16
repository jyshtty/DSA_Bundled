"""
Problem: Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Description:
    Given an unsorted array of integers nums, return the length of the
    longest consecutive elements sequence. Must run in O(n) time.

Examples:
    Input:  nums = [100, 4, 200, 1, 3, 2]    Output: 4  (sequence: 1,2,3,4)
    Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  Output: 9

Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # O(1) lookup; converting to set also removes duplicates
        best = 0

        for num in num_set:
            # only start counting from the beginning of a sequence;
            # skipping if (num-1) exists avoids re-counting the same sequence
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                best = max(best, length)

        return best
