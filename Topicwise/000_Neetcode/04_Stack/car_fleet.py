"""
Problem: Car Fleet
Link: https://leetcode.com/problems/car-fleet/

Description:
    n cars travel toward a target destination at various positions and speeds.
    A car fleet is a group of cars that arrive together. If a faster car catches
    a slower car before the target, they form one fleet (the faster car slows down).
    Return the number of car fleets that reach the target.

Examples:
    Input:  target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    Output: 3

    Input:  target = 10, position = [3], speed = [3]
    Output: 1

Constraints:
    n == position.length == speed.length
    1 <= n <= 10^5
    0 <= position[i] < target
    1 <= speed[i] <= 10^6
    All positions are unique.
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by position descending so we process cars closest to target first
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            stack.append(time)
            # if current car arrives no later than the car ahead, it merges into that fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
