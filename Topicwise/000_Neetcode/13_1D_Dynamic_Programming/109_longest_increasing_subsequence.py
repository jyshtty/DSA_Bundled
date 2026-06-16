"""
Problem: Longest Increasing Subsequence
Link: https://leetcode.com/problems/longest-increasing-subsequence/

Description:
    Given an integer array nums, return the length of the longest strictly
    increasing subsequence.

Examples:
    Input:  nums = [10,9,2,5,3,7,101,18]    Output: 4  ([2,3,7,101])
    Input:  nums = [0,1,0,3,2,3]            Output: 4
    Input:  nums = [7,7,7,7,7]              Output: 1

Constraints:
    1 <= nums.length <= 2500
    -10^4 <= nums[i] <= 10^4
"""

from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # patience sorting: tails[i] is the smallest tail of all increasing subsequences of length i+1
        tails = []
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num  # replace to keep tails as small as possible for future extensions
        return len(tails)
