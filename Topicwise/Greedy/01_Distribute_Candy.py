class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        left = []
        left.append(1)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                left.append(left[-1] + 1)
            else:
                left.append(1)

        right = []
        right.append(1)
        for i in range(len(A) - 2, -1, -1):
            if A[i + 1] < A[i]:
                right.append(right[-1] + 1)
            else:
                right.append(1)

        right = right[::-1]

        ans = []

        for i in range(len(left)):
            ans.append(max(left[i], right[i]))

        return ans

A = [1, 2]
obj = Solution()
print(obj.candy(A))
