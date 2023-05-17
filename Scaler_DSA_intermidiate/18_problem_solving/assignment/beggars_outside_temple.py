"""
Input:
A = 5, B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

Return: [10, 55, 45, 25, 25]

Explanation:
=> First devotee donated 10 coins to beggars ranging from 1 to 2. Final amount in each beggars pot after first devotee: [10, 10, 0, 0, 0]

=> Second devotee donated 20 coins to beggars ranging from 2 to 3. Final amount in each beggars pot after second devotee: [10, 30, 20, 0, 0]

=> Third devotee donated 25 coins to beggars ranging from 2 to 5. Final amount in each beggars pot after third devotee: [10, 55, 45, 25, 25]

"""
[10, 35, -20, 0, -25]

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers

    def prefix_sum(self, C):
        sum = 0
        D  = []
        for i in C:
            sum = sum + i
            D.append(sum)
        return D

    def solve(self, A, B):
        C = [0] * (A+1)
        for i in range(len(B)):
            C[B[i][0]-1] = C[B[i][0]-1] + B[i][2]
            C[B[i][1]] = C[B[i][1]] - B[i][2]
        return self.prefix_sum(C[:-1])

if __name__ == "__main__":
    A = 5
    B = [[1, 2, 100],[2, 5, 100],[3, 4, 100]]
    obj = Solution()
    print(obj.solve(A, B))

