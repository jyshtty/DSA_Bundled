# Problem Description
# You are given an array A of integers that represent the lengths of ropes.
#
# You need to connect these ropes into one rope. The cost of joining two ropes equals the sum of their lengths.
#
# Find and return the minimum cost to connect these ropes into one rope.
#
# Example Input
# Input 1:
#
#  A = [1, 2, 3, 4, 5]
# Input 2:
#
#  A = [5, 17, 100, 11]
#
#
# Example Output
# Output 1:
#
#  33
# Output 2:
#
#  182

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        cost = 0
        from heapq import heappush, heappop, heapify
        heapify(A)
        while True:
            rope1 = heappop(A)
            rope2 = heappop(A)

            cost += rope1 + rope2

            if not A:
                return cost
            else:
                heappush(A, rope1 + rope2)

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    obj = Solution()
    print(obj.solve())

