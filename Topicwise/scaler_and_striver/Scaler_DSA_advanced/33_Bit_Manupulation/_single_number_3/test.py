# # # # def to_binary(b):
# # # #     binary = []
# # # #     while b > 0:
# # # #         if b % 2:
# # # #             binary.append(1)
# # # #         else:
# # # #             binary.append(0)
# # # #         b = b//2
# # # #     binary = binary[::-1]
# # # #     a = int(''.join([str(i) for i in binary]))
# # # #     return a
# # # # print(to_binary(358))
# # #
# # # def A():
# # #     print('l1')
# # #     B()
# # #     print('l2')
# # #
# # # def B():
# # #     print('l3')
# # #     C()
# # #     print('l4')
# # #
# # # def C():
# # #     print('l5')
# # #
# # # A()
# # #
# # # def print_increasing(n):
# # #     if n == 0:
# # #         return 0
# # #     return n * (10 ** n) + print_increasing(n-1)
# # #     # print(n)
# # #
# # # print(print_increasing(5))
# #
# # def decimal_to_binary(n):
# #     strg = ''
# #     if n == 0:
# #         return ''
# #     strg = decimal_to_binary(n//2)
# #     strg = strg + str(n%2)
# #     return strg
# #
# #
# #
# #
# # print(decimal_to_binary(8))
#
# def StringChallenge(strParam):
#   strParam1 = [char for char in strParam]
#   if len(strParam1) == 0:
#     return
#   s1 = ''
#   s1 += strParam1[0].lower()
#   for i in range(1, len(strParam1)):
#     if (strParam1[i] == ' '):
#       s1 += strParam1[i + 1].upper()
#       i += 1
#     elif (strParam1[i].isalnum() == False):
#       s1 += strParam1[i + 1].upper()
#       i += 1
#     elif(strParam1[i-1] != ' ' and strParam1[i-1].isalnum() != False):
#       s1 += strParam1[i]
#
#   # code goes here
#   print(s1, 'aBCDEFG')
# # keep this function call here
# # ('aBCDEeFf%g', 'aBCDEFG')
# # strParam = 'cats AND*Dogs-are Awesome'
# strParam = "e-is Ajay"
# # strParam = 'My name is Ajay'
#


# StringChallenge(strParam)
#
# def binary_search(arr, x):
# 	l = 0
# 	r = len(arr)-1
# 	while l <= r:
# 		mid = (l + r)//2
# 		if arr[mid] == x:
# 			return x
# 		elif arr[mid] < x:
# 			l = mid + 1
# 		else:
# 			r = mid -1
# 	return 'not Found'
# arr = [1,2,3,4,5,6,7]
# print(binary_search(arr, 3))

class Solution:
  # @param A : list of list of integers
  # @param B : integer
  # @return a list of list of integers
  def solve(self, A, B):
    list01 = []
    res = []
    for i in range(len(A)):
      sum = abs(A[i][0]) + abs(A[i][1])
      list01.append((sum, i))
    list01.sort(reverse = True)

    for i in range(B):
      res.append(A[list01[i][1]])
    res.sort()
    return res


A.sort()
        for i in range(len(A) - 1, 0, -1):
            if A[i] != A[i - 1]:
                return A[i - 1] % A[i]
        return 0A.sort()
        for i in range(len(A) - 1, 0, -1):
            if A[i] != A[i - 1]:
                return A[i - 1] % A[i]
        return 0

if __name__ == "__main__":
  A = [[26, 41],[40, 47],[47, 7],[50, 34],[18, 28]]
  B= 5
  obj = Solution()
  print(obj.solve(A,B))
