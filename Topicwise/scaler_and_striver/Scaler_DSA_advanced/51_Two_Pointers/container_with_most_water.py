class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):

        if len(A) == 1:
            return 0
        i = 0
        j = len(A) - 1
        water = 0
        while i < j:
            water = max(water, (j-i)*(min(A[i], A[j])))
            if A[i] < A[j]:
                i += 1
            elif A[j] < A[i]:
                j -= 1
            else:
                i += 1
                j += 1
        return water

if __name__ == "__main__":
    A = [1, 5, 4, 3]
    obj = Solution()
    print(obj.maxArea(A))