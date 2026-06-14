"""
Problem: Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/

Description:
    Given an integer array nums and an integer k, return the k most
    frequent elements. You may return the answer in any order.

Examples:
    Input:  nums = [1, 1, 1, 2, 2, 3], k = 2    Output: [1, 2]
    Input:  nums = [1], k = 1                    Output: [1]

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    k is in the range [1, number of unique elements]
    The answer is guaranteed to be unique.
"""

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # bucket[i] holds all numbers that appear exactly i times
        # max frequency can't exceed len(nums), so we size buckets accordingly
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        # iterate from highest frequency downward to collect top-k
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
