from heapq import heappop, heappush, heapify

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        new = [[A[i], i] for i in range(len(A))]
        heapify(new)
        i = 0

        while i != B:
            min, index = heappop(new)

            new_min = min + A[index]

            heappush(new, [new_min, index])

            i += 1

        return (max(new)[0])

A = [5, 1, 4, 2]
B = 5
obj = Solution()
print(obj.solve(A,B))




