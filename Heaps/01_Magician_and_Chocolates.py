# Problem Description
# Given N bags, each bag contains Bi chocolates. There is a kid and a magician.
# In a unit of time, the kid can choose any bag i, and eat Bi chocolates from it, then the magician will fill the ith bag with floor(Bi/2) chocolates.
#
# Find the maximum number of chocolates that the kid can eat in A units of time.
#
#
# Example Input
# Input 1:
#  A = 3
#  B = [6, 5]

# Input 2:
#  A = 5
#  b = [2, 4, 6, 8, 10]

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        from heapq import heapify, heappop, heappush
        new_heap = [-1 * i for i in B]
        heapify(new_heap)

        time = 0
        sum = 0
        while time != A:
            x = heappop(new_heap)
            sum += x

            heappush(new_heap, x//2)
            time += 1

        return  ((-sum) % (10**9 + 7))

if __name__ == "__main__":
    A = 3
    B = [6, 5]
    obj = Solution()
    print(obj.nchoc(A, B))

