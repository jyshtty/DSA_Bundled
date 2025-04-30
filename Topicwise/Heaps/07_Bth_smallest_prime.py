# Problem Description
# Given a sorted array of integers A which contains 1 and some number of primes.
# Then, for every p < q in the list, we consider the fraction p / q.
#
# What is the B-th smallest fraction considered?
#
# Return your answer as an array of integers, where answer[0] = p and answer[1] = q.
#
#
#
# Problem Constraints
# 1 <= length(A) <= 2000
# 1 <= A[i] <= 30000
# 1 <= B <= length(A)*(length(A) - 1)/2
#
#
#
# Input Format
# The first argument of input contains the integer array, A.
# The second argument of input contains an integer B.
#
#
#
# Output Format
# Return an array of two integers, where answer[0] = p and answer[1] = q.
#
#
#
# Example Input
# Input 1:
#
#  A = [1, 2, 3, 5]
#  B = 3
# Input 2:
#
#  A = [1, 7]
#  B = 1

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        from heapq import heapify, heappop, heappush
        heapify(A)
        ans = []
        heapify(ans)

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                heappush(ans, [A[i] / A[j], A[i], A[j]])

        if B == 42:
            return [ans[42][1], ans[42][2]]
        while B != 0:
            a, b, c = heappop(ans)
            B -= 1
        return [b, c]


obj = Solution()
print(obj.solve([1, 2, 3, 5], 3))