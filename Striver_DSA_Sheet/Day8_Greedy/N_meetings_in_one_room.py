# Approach
#
# 1. constuct a list of list with [[endtime, (starttime, endtime, index+1)]]      index + 1 as it is 1 based indexing, and we will loose index when we sort in next step
# 2. sort it.
# 3. take a variable current end time.
# 4. initially current end time is 0
# 5. when current end time is < ith start time, include the meeting interval in ans array and update current end time as e1 (end time of that interval)
# 6. Return ans array