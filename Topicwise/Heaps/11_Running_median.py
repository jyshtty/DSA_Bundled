# Steps
# 1. # create left dabba, # create right dabba
# 2. # make sure everything of left dabba is less than right
# 3. # make sure length of left -  length of right Is not greater than 1
# 4. # return left dabba top root

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        from heapq import heapify, heappush, heappop
        ans = [A[0]]
        max_heap = []  # create left dabba
        min_heap = []  # create right dabba

        heapify(max_heap)
        heapify(min_heap)

        heappush(max_heap, -1 * A[0])

        for i in range(1, len(A)):
            # make sure everything of left dabba is less than right
            if A[i] <= -max_heap[0]:
                heappush(max_heap, -1 * A[i])
            else:
                heappush(min_heap, A[i])

            # make sure length of right is not greater than length of left
            if len(min_heap) > len(max_heap):
                x = heappop(min_heap)
                heappush(max_heap, -1 * x)

            # make sure length of left -  length of right Is not greater than 1
            if len(max_heap) - len(min_heap) > 1:
                x = heappop(max_heap)
                heappush(min_heap, -1 * x)

            ans.append(-max_heap[0])
        return ans
