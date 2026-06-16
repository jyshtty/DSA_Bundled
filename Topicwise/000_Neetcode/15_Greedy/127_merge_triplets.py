"""
Problem: Merge Triplets to Form Target Triplet
Link: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

Description:
    A triplet is [a, b, c]. Merging two triplets [a1,b1,c1] and [a2,b2,c2]
    gives [max(a1,a2), max(b1,b2), max(c1,c2)].
    Given a list of triplets and a target, return true if any selection
    of triplets can be merged to equal target.

Examples:
    Input:  triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]   Output: True
    Input:  triplets = [[3,4,5],[4,5,6]], target = [3,2,5]           Output: False

Constraints:
    1 <= triplets.length <= 10^5
    triplets[i].length == target.length == 3
    1 <= ai, bi, ci, x, y, z <= 1000
"""

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # only consider triplets where no element exceeds target (others would corrupt the merge)
        result = [0, 0, 0]
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                result = [max(result[i], t[i]) for i in range(3)]

        return result == target
