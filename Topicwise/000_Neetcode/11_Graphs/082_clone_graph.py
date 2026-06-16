"""
Problem: Clone Graph
Link: https://leetcode.com/problems/clone-graph/

Description:
    Given a reference of a node in a connected undirected graph, return a
    deep copy (clone) of the graph.

Examples:
    Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]    Output: [[2,4],[1,3],[2,4],[1,3]]
    Input:  adjList = [[]]                          Output: [[]]

Constraints:
    1 <= nodes.length <= 100
    1 <= Node.val <= 100
    Node.val is unique for each node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        clones = {}  # maps original node -> its clone; prevents infinite loops in cycles

        def dfs(n):
            if n in clones:
                return clones[n]
            clone = Node(n.val)
            clones[n] = clone  # register before visiting neighbors to handle cycles
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)
