class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, B, A):
        for i in range(len(A)):
            A[i] = (A[i], i)
        A.sort()


        new_B = [0] * len(B)
        for i in range(len(B)):
            new_B[i] = B[A[i][1]]

        new_A = [i[0] for i in A]
        ans = 1

        i = 0
        j = 1
        while i < len(new_A) - 1 and j < len(new_B):
            if new_A[i] <= new_B[j]:
                ans += 1
                i = j
            j += 1
        return ans

A = [1, 5, 7, 1]
B = [7, 8, 8, 8]
obj = Solution()
print(obj.solve(A, B))