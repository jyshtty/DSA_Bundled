# insert new interval in the list of non-overlapping intervals and merge if necessary
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = len(intervals)
        ans = []
        for i in range(l):
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                                max(newInterval[1], intervals[i][1])]
        ans.append(newInterval)
        return ans
        