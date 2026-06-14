"""
Problem: Sliding Window Maximum
Link: https://leetcode.com/problems/sliding-window-maximum/

Description:
    Given an array nums and an integer k, return an array of the maximum
    value in each sliding window of size k.

Examples:
    Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3    Output: [3,3,5,5,6,7]
    Input:  nums = [1], k = 1                      Output: [1]

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
"""

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices; front always holds the index of the window's max
        result = []

        for i, num in enumerate(nums):
            # remove indices that are out of the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # remove indices whose values are smaller than current — they can never
            # be the max while the current element is in the window
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(i)

            # start recording once the first full window is formed
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
