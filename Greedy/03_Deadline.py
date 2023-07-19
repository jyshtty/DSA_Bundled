# max
# 1e6 - merory limit
# 2 * 1e8 -- TLE
# 1e9 operation
#
# 2e8 max operation we can perform per sec.


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        c = [(B[i], A[i]) for i in range(len(A))]
        c.sort(reverse = True)
        sum = 0
        arr = [0] * (max(A)+1)
        # arr[3] = 0
        arr[0] = 100
        for i in c:
            index = i[1]
            while arr[index] != 100:
                if arr[index] == 0:
                    arr[index] = 1
                    sum += i[0]
                    break

                elif arr[index] == 1:
                    index -= 1
        return sum

A = [1,1,5,2,6]
B = [10,15,100, 100,150]
# arr = [100, 1 ,1, 0, 0, 1, 1 ]
obj = Solution()
print(obj.solve(A, B))