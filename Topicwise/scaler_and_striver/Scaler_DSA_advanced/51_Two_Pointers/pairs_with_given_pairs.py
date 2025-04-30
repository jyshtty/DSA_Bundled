class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        A = list(set(A))
        A.sort()
        i = 0
        j = 0
        n = len(A)
        count = 0
        while j < n:
            if A[j] - A[i] < B:
                j += 1
            elif A[j] - A[i] > B:
                i += 1
            else:
                if i != j:
                    count += 1
                    i += 1
                    j += 1
                else:
                    j += 1
                while i+1 < n and A[i+1] == A[i]:
                    i += 1
                while j+1 < n and A[j+1] == A[j]:
                    j += 1


        return count

if __name__ == "__main__":
    A = [1,2]
    B = 0
    obj = Solution()
    print(obj.solve(A, B))



