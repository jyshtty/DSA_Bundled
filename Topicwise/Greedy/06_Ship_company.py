class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        from heapq import heapify, heappush, heappop
        min_hp = list(C)
        heapify(min_hp)
        min_cost = 0
        for i in range(A):
            x = heappop(min_hp)
            min_cost += x
            if x-1 !=0:
                heappush(min_hp, x - 1)

        max_hp = [-i for i in C]
        heapify(max_hp)
        max_cost = 0
        for i in range(A):
            x = heappop(max_hp)
            max_cost += x
            if x + 1 != 0:
                heappush(max_hp, x + 1)

        return [min_cost,-max_cost]

obj = Solution()
A = 10
B = 5
C = [10, 3, 3, 1, 2]
print(obj.solve(A,B,C))