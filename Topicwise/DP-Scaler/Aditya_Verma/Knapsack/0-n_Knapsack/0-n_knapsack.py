# 0-1 Knapsack Problem
# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
# You are given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.
# Also, you are given an integer C which represents knapsack capacity.

# example: 
# Input:
# A = 10
# B = [ 5 ]
# C = [ 10 ]
# Output: 10

# Explanation:
# We can take the only item available with weight 5 and value 10.
# So the maximum value we can obtain is 10.
# Your Task:
# You don't need to read input or print anything.
# Your task is to complete the function solve() which takes values and weights of items and knapsack capacity as input parameters and returns the maximum value that can be put in the knapsack.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        A, B, C = B, C, A
        dp = [[0 for i in range(A + 1)] for j in range(len(C) + 1)]

        for index in range(1, len(C) + 1):
            for j in range(1, A + 1):
                dp[index][j] = dp[index - 1][j]
                if j >= B[index - 1]:
                    dp[index][j] = max(dp[index][j], dp[index][j - C[index - 1]] + B[index - 1])
        return dp[len(C)][A]

# A = 10
# B = [ 5 ]
# C = [ 10 ]

A, B, C = B, C, A

print(A)
print(B)
print(C)
