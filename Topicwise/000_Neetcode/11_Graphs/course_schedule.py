"""
Problem: Course Schedule
Link: https://leetcode.com/problems/course-schedule/

Description:
    There are numCourses (0 to n-1). Given prerequisites [a, b] meaning
    you must take b before a, return true if you can finish all courses.

Examples:
    Input:  numCourses = 2, prerequisites = [[1,0]]        Output: True
    Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]  Output: False

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    No duplicate prerequisites.
"""

from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        # 0 = unvisited, 1 = in current DFS path (cycle detection), 2 = fully processed
        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:
                return False  # back edge — cycle found
            if state[node] == 2:
                return True   # already verified safe

            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = 2
            return True

        return all(dfs(i) for i in range(numCourses))
