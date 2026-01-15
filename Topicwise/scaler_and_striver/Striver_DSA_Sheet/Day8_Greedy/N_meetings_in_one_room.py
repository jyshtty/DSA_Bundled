# N Meetings in One Room
# There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
# What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?
# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
# Example:
# Input: N = 6, start[] = {1,3,0,5,8,5}, end[] = {2,4,6,7,9,9}
# Output: 4
# Approach: Sort by end time, greedy select
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Implementation:


# Approach
#
# 1. constuct a list of list with [[endtime, (starttime, endtime, index+1)]]      index + 1 as it is 1 based indexing, and we will loose index when we sort in next step
# 2. sort it.
# 3. take a variable current end time.
# 4. initially current end time is 0
# 5. when current end time is < ith start time, include the meeting interval in ans array and update current end time as e1 (end time of that interval)
# 6. Return ans array