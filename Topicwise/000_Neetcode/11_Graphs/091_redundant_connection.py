"""
Problem: Redundant Connection
Link: https://leetcode.com/problems/redundant-connection/

Description:
    In a tree with n nodes labeled 1..n, one extra edge was added creating a cycle.
    Given edges, return the redundant edge. If multiple answers, return the last one.

Examples:
    Input:  edges = [[1,2],[1,3],[2,3]]     Output: [2,3]
    Input:  edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]   Output: [1,4]

Constraints:
    n == edges.length
    3 <= n <= 1000
    edges[i].length == 2
    1 <= ai < bi <= edges.length
    ai != bi, no repeated edges
"""

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression (halving)
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False  # already connected — this edge creates a cycle
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            rank[px] += rank[py]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
