from collections import Counter
from math import sqrt


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 1:
            return 1
        curr = []
        ans = 0
        fm = Counter(A)

        def new(curr, fm):
            if len(curr) == len(A):
                if self.squareful_array(curr):
                    nonlocal ans
                    ans += 1

            for k, v in fm.items():
                if v > 0:
                    fm[k] -= 1
                    new(curr + [k], fm)
                    fm[k] += 1

        new(curr, fm)
        return ans

    def isSquare(self, n):
        sq_root = sqrt(n)
        return (sq_root - int(sq_root)) == 0

    def squareful_array(self, A):
        i = 0
        j = i + 1
        while j < len(A):
            temp = A[i] + A[j]
            if self.isSquare(temp):
                i += 1
                j += 1
            else:
                return False
        return True

a = Solution()
# print(a.solve([ 530786350, 499920803, 736695757, 626782894, 908847028, 697150472, 33385161, 566692139 ]))
# print(a.solve([2,2,2]))
print(a.solve([1, 17, 8]))










