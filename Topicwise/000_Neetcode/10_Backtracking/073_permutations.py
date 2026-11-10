"""
Problem: Permutations
Link: https://leetcode.com/problems/permutations/

Description:
    Given an array nums of distinct integers, return all possible permutations.
    You can return the answer in any order.

Examples:
    Input:  nums = [1,2,3]    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    Input:  nums = [0,1]      Output: [[0,1],[1,0]]

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All integers are unique.
"""

class Solution:
	# @param A : list of integers
	# @return a list of list of integers

	def generate(self, index, curr):
		if index == len(self.A):
			self.output.append(list(curr))
			# print(curr)
			return
		for i in range(len(self.A)):
			flag = 0
			for j in range(index):
				if curr[j] == self.A[i]:
					flag = 1
			if flag == 0:
				curr[index] = self.A[i]
				self.generate(index + 1, curr)

	def permute(self, A):
		self.A = A
		self.output = []
		curr = [float('inf') for i in range(len(A))]
		self.generate(0, curr)
		return self.output
