"""
Problem: Detect Squares
Link: https://leetcode.com/problems/detect-squares/

Description:
    Design a data structure that counts axis-aligned squares from points.
    add(point): Adds a point.
    count(point): Returns number of ways to choose 3 points from the data
    structure such that they form an axis-aligned square with the given point.

Examples:
    detectSquares = DetectSquares()
    detectSquares.add([3,10]); detectSquares.add([11,2]); detectSquares.add([3,2])
    detectSquares.count([11,10])  # 1
    detectSquares.count([14,8])   # 0
    detectSquares.add([11,2])
    detectSquares.count([11,10])  # 2

Constraints:
    point.length == 2
    0 <= x, y <= 1000
    At most 3000 calls total.
"""

from collections import defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        self.pt_count = defaultdict(int)   # (x, y) -> count
        self.x_pts = defaultdict(set)      # x -> set of y values

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pt_count[(x, y)] += 1
        self.x_pts[x].add(y)

    def count(self, point: List[int]) -> int:
        px, py = point
        total = 0

        # fix the diagonal point (px, y3) — same x as query, different y
        for y3 in self.x_pts[px]:
            side = abs(py - y3)
            if side == 0:
                continue
            # the square has two possible orientations: x4 = px +/- side
            for x4 in [px + side, px - side]:
                # need (x4, py) and (x4, y3) to exist
                total += self.pt_count[(x4, py)] * \
                         self.pt_count[(x4, y3)] * \
                         self.pt_count[(px, y3)]

        return total
