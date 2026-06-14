"""
Problem: Graph Valid Tree
Link: https://leetcode.com/problems/graph-valid-tree/

Description:
    Given n nodes and a list of undirected edges, return true if the edges
    form a valid tree (connected and no cycle).

Examples:
    Input:  n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]    Output: True
    Input:  n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]    Output: False

Constraints:
    1 <= n <= 2000
    0 <= edges.length <= 5000
"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree must have exactly n-1 edges; more means a cycle, fewer means disconnected
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  # same component — adding this edge creates a cycle
            parent[ra] = rb

        return True
