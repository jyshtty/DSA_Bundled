"""
Problem: Course Schedule II
Link: https://leetcode.com/problems/course-schedule-ii/

Description:
    Return an ordering of courses to finish all numCourses given prerequisites.
    If impossible (cycle), return an empty array.

Examples:
    Input:  numCourses = 2, prerequisites = [[1,0]]           Output: [0,1]
    Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3] or [0,1,2,3]

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= numCourses * (numCourses - 1)
"""

from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses
        order = []

        def dfs(node):
            if state[node] == 1:
                return False  # cycle detected
            if state[node] == 2:
                return True

            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = 2
            order.append(node)  # append after all descendants are processed (topological sort)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order[::-1]  # reverse because we append in post-order
