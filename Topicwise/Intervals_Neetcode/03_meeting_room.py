# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
# determine if a person could add all meetings to their schedule without any conflicts.

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        l = len(intervals)

        for i in range(1,l):
            if intervals[i-1].end > intervals[i].start:
                return False
        return True