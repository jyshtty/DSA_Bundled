"""
Problem: Task Scheduler
Link: https://leetcode.com/problems/task-scheduler/

Description:
    Given a list of tasks and a cooldown n, find the minimum intervals
    needed to finish all tasks. Same tasks must be at least n intervals apart.
    CPU can be idle.

Examples:
    Input:  tasks = ["A","A","A","B","B","B"], n = 2    Output: 8
    Input:  tasks = ["A","A","A","B","B","B"], n = 0    Output: 6

Constraints:
    1 <= tasks.length <= 10^4
    tasks[i] is an uppercase English letter.
    0 <= n <= 100
"""

from typing import List
from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown_queue = []  # stores (-count, available_time)

        while max_heap or cooldown_queue:
            time += 1
            if max_heap:
                count = heapq.heappop(max_heap) + 1  # +1 because count is negative
                if count != 0:
                    cooldown_queue.append((count, time + n))

            # release tasks whose cooldown has expired
            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(max_heap, cooldown_queue.pop(0)[0])

        return time
