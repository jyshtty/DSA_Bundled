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
        c = [(A[i], B[i]) for i in range(len(A))]
        c.sort()
        sum = 0

        from heapq import heapify, heappop, heappush
        hp = []
        heapify(hp)
        days = 0

        for i in c:
            time = i[0]
            if time > days:
                heappush(hp, i[1])
                days += 1
            else:
                if hp[0] < i[1]:
                    heappop(hp)
                    heappush(hp, i[1])
        for i in hp:
            sum += i
            sum = sum % (10**9 + 7)
        return sum

A = [1,1,5,2,6]
B = [10,15,100, 100,150]
# arr = [100, 1 ,1, 0, 0, 1, 1 ]
obj = Solution()
print(obj.solve(A, B))