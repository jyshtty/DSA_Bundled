# 0/1 Knapsack Problem using Recursion
# Given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
# Example:
# Input:
# N = 4, W = 50
# values[] = {60, 100, 120, 240}
# weights[] = {10, 20, 30, 40}
# Output: 340
# Explanation: We can take items with weight 10 and 40 kg and total value will be 60 + 240 = 300.  

val = [1,2,3,4]
weight = [10,20,30,40]

def knapsack(W, N):
    if W == 0 or N == 0:
        return 0
    if weight[N-1] <= W:
        return max(knapsack(W-weight[N-1], N-1) + val[N-1], knapsack(W, N-1))
    else:
        return knapsack(W, N-1)

print(knapsack(50, 4))