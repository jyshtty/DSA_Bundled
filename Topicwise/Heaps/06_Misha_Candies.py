# Misha loves eating candies. She has been given N boxes of Candies.
# She decides that every time she will choose a box having the minimum number of candies, eat half of the candies and put the remaining candies in the other box that has the minimum number of candies.
# Misha does not like a box if it has the number of candies greater than B so she won't eat from that box. Can you find how many candies she will eat?
# NOTE 1: If a box has an odd number of candies then Misha will eat the floor(odd / 2).
# NOTE 2: The same box will not be chosen again.
#
# Example Input
# Input 1:
#  A = [3, 2, 3]
#  B = 4
# Input 2:
#  A = [1, 2, 1]
#  B = 2
#
# Example Output
# Output 1:
#  2
# Output 2:
#  1

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        from heapq import heapify, heappush, heappop
        heapify(A)
        ans = 0

        while A[0] <= B:
            min1 = heappop(A)
            min2 = heappop(A) if A else 0
            ate = min1 // 2
            left = min1 - (ate)
            ans += ate
            to_add = left + min2
            heappush(A, to_add)touch
        return ans

obj = Solution()
print(obj.solve(A, B))