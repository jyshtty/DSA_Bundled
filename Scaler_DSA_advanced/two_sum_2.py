# # # def two_Sum(arr, target):
# # #     low = 0
# # #     high = len(arr) - 1
# # #     while low <= high:
# # #         mid = low + (high - low)//2
# # #         if arr[mid] == target:
# # #             return [mid, 'found']
# # #         elif target < arr[mid]:
# # #             high = mid -1
# # #         else:
# # #             low = mid + 1
# # #     return [high,'Not found']
# # #
# # #
# # #
# # # arr = [2,4,5,6,7,9,10]
# # # target = 8
# # # print(solve(arr, target))
# # #
# # #
# # #
# #
# # def prime(a):
# #     iprime = [True] * a
# #     iprime[0], iprime[1] = False, False
# #     for i in range(2, a):
# #         j = 2
# #         while j * i < a:
# #             iprime[j * i] = False
# #             j = j + 1
# #     for i in range(len(iprime)):
# #         if iprime[i] == True:
# #             print(i)
# #
# #
# # prime(27)
# # n = 3
# # A = [0,0,0]
# # arr = [1,2,3]
# # temp = [i for i in arr]
# # def generate(index):
# #     if index == n:
# #         print(A)
# #         return
# #
# #     A[index] = arr[index]
# #     generate(index + 1)
# #     A[index] = arr[index]
# #     generate(index + 1)
# #
# # generate(0)
#
# # def foo():
# #     if 0 == False:
# #         print("Aay")
# #         return
# #
# # foo()
#
# curr = [-10, -10,-10]
# A = [1,2,3]
# output = []
# def generate(index):
# 	if index == len(A):
# 		output.append(curr)
# 		return
# 	for i in range(len(A)):
# 		flag = 0
# 		for j in range(index):
# 			if curr[j] == A[i]:
# 				flag = 1
# 		if flag == 0:
# 			curr[index] = A[i]
# 			generate(index + 1)

#
# generate(0)
# print(output)

# def deco(func):
# 	"""
#
# 	:rtype: object
# 	"""
# 	def wrapped():
# 		print("Welcome")
# 		func()
# 		print("Thank you")
# 	return wrapped
#
# @deco
# def foo():s
# 	print("Ajay")


# foo()

class Solution:
	# @param A : list of integers
	# @return a list of list of integers

	def generate(self, index, curr):
		if index == len(self.A):
			# self.output.append(list(curr))
			print(curr)
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


obj = Solution()
# print(obj.permute([1,2,3]))
print(obj.permute([ 508, 503, 412, 895, 256, 89, 245, 567, 9, 123 ]))