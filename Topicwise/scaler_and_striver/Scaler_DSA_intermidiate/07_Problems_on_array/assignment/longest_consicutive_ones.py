class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        A = [int(i) for i in A]
        left = [0] * len(A)
        right = [0] * len(A)

        l = 0
        r = len(A)-1

        while (l < len(A)):
            if A[l] == 1:
                if l != 0:
                    left[l] = left[l-1] + A[l]
                else:
                    left[l] =  A[l]
            elif A[l] != 1:
                left[l] = 0
            if A[r] == 1:
                if r != len(A)-1:
                    right[r]  = right[r+1] + A[r]
                else:
                    right[r] = A[r]
            elif A[r] != 1:
                right[r] = 0

            l += 1
            r -= 1
        ans = 0
        countofTotalOnes = A.count(1)
        right.append(0)

        left[:0] = [0]
        right[:0] = [0]

        for i in range(len(A)):
            if i == A[i]:
                ans = max(ans, (left[i+1] + right[i+1] - 1))
            else:
                if (left[i] + right[i+2]) == countofTotalOnes:
                    ans = max(ans, (left[i]) + right[i+2])
                else:
                    ans = max(ans, (left[i]) + right[i + 2] + 1)
        return ans

if __name__ == "__main__":
    A = "11100"
    obj = Solution()
    print(obj.solve(A))



