# leetcode 46: Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# https://leetcode.com/problems/permutations/
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Approach: Backtracking
# Time Complexity: O(n!)
# Space Complexity: O(n!)
# Implementation:


# generate all permutation of [1,2,3]

def solve(arr):
    curr = [-1] * len(arr)
    ans = []
    def generate(index):
        if index == len(curr):
            ans.append(curr)
        for i in range(len(arr)):
            flag = 0
            for j in range(index):
                if curr[j] == arr[i]:
                    flag = 1
                    break
            if flag == 0:
                curr[index] = arr[i]
                generate(index+1)
    generate(0)
    return ans
