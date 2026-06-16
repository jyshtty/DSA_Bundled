"""
Problem: Number of Connected Components in an Undirected Graph
Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Description:
    Given n nodes (0 to n-1) and an array of edges, return the number of
    connected components in the graph.

Examples:
    Input:  n = 5, edges = [[0,1],[1,2],[3,4]]    Output: 2
    Input:  n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]    Output: 1

Constraints:
    1 <= n <= 2000
    1 <= edges.length <= 5000
    No duplicate edges or self-loops.
"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression: halves future traversal depth
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return 0  # already same component
            parent[ra] = rb
            return 1  # merged two components

        return n - sum(union(a, b) for a, b in edges)
