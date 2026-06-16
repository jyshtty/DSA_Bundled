"""
Problem: Koko Eating Bananas
Link: https://leetcode.com/problems/koko-eating-bananas/

Description:
    Koko can eat at most k bananas per hour. Given piles of bananas and h
    hours, return the minimum integer k such that Koko can eat all bananas
    within h hours.

Examples:
    Input:  piles = [3,6,7,11], h = 8    Output: 4
    Input:  piles = [30,11,23,4,20], h = 5    Output: 30

Constraints:
    1 <= piles.length <= 10^4
    piles.length <= h <= 10^9
    1 <= piles[i] <= 10^9
"""

from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)  # speed ranges from 1 to largest pile

        while left < right:
            mid = left + (right - left) // 2
            # hours needed at speed mid: ceil(pile/mid) per pile
            hours = sum(math.ceil(p / mid) for p in piles)
            if hours <= h:
                right = mid   # mid works; try slower (smaller k)
            else:
                left = mid + 1

        return left
