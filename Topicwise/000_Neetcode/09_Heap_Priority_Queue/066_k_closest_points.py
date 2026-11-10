"""
Problem: K Closest Points to Origin
Link: https://leetcode.com/problems/k-closest-points-to-origin/

Description:
    Given an array of points on a plane, return the k closest points to
    the origin (0, 0). Distance is Euclidean. Order of answer doesn't matter.

Examples:
    Input:  points = [[1,3],[-2,2]], k = 1    Output: [[-2,2]]
    Input:  points = [[3,3],[5,-1],[-2,4]], k = 2    Output: [[3,3],[-2,4]]

Constraints:
    1 <= k <= points.length <= 10^4
    -10^4 <= xi, yi <= 10^4
"""

import heapq
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        pq = []
        for p in A:
            heapq.heappush(pq, [-p[0] * p[0] - p[1] * p[1], p])
            print(pq)

            if len(pq) > B: # Important - just make sure points with highest distance from (0,0) is poped out when total count is greater than B.
                heapq.heappop(pq)
        print(pq)
        return [p for _, p in pq]

A = [
       [1, 3],
       [-2, 2]
     ]
B = 1
obj = Solution()
print(obj.solve(A, B))
