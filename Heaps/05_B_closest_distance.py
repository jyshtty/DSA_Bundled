# Problem Description
# We have a list A of points (x, y) on the plane. Find the B closest points to the origin (0, 0).
#
# Here, the distance between two points on a plane is the Euclidean distance.
#
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in.)
#
# NOTE: Euclidean distance between two points P1(x1, y1) and P2(x2, y2) is sqrt( (x1-x2)2 + (y1-y2)2 ).

# Input 1:
#
#  A = [
#        [1, 3],
#        [-2, 2]
#      ]
#  B = 1
# Input 2:
#
#  A = [
#        [1, -1],
#        [2, -1]
#      ]
#  B = 1
#
#
# Example Output
# Output 1:
#
#  [ [-2, 2] ]
# Output 2:
#
#  [ [1, -1] ]

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