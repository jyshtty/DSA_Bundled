# # # # a = [1,2,3,4,5]
# # # #
# # # # b = [5,1,2,7,5]
# # # #
# # # # c = [1,-1,-1,]
# # # #
# # # # def foo(a,b):
# # # #     ls = []
# # # #     for i in range(len(a)):
# # # #         if a[i] > b[i]:
# # # #             ls.append(-1)
# # # #         elif a[i] < b[i]:
# # # #             ls.append(1)
# # # #         else:
# # # #             ls.append(0)
# # # #     return ls
# # # # print(foo(a,b))
# # #
# # # # a = 100
# # # #
# # # # def foo():
# # # #     for i in range(10):
# # # #         a = i + 1
# # # #     print(a)
# # # #     return a
# # # #
# # # # foo()
# # # # print(a)
# # #
# # # # s = [1,2,3,4]
# # # # r = [0] * len(s)
# # # # sum = 0
# # # # for i in range(len(s)):
# # # #     sum = sum + s[i]
# # # #     r[i] = sum
# # # # print(r)
# # # # ls = []
# # # # a = [1,2,3,4,5]
# # # # for i in a:
# # # #     print(dir(a))
# # # #     ls.append(i)
# # # # print(ls)
# # #
# # # class Solution:
# # #     def merge(self, intervals):
# # #         ls = [intervals[0]]
# # #         i = 0
# # #         for i in range(1,len(intervals)):
# # #             if ls[-1][1] > intervals[i][0]:
# # #                 ls[-1] = [  ls[-1][0], max(intervals[i][1],ls[-1][1]) ]
# # #             else:
# # #                 ls.append(intervals[i])
# # #         return ls
# # #
# # # if __name__ == "__main__":
# # #     intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# # #     obj = Solution()
# # #     print(obj.merge(intervals))
# #
# #
# # # def foo(A):
# # #     ls = [0]* (len(A) + 1)
# # #     for i in A:
# # #         ls[i] += 1
# # #     print(ls)
# # #     for i in range(1, len(ls)):
# # #         if ls[i] == 0:
# # #             print(f"{i} is missing")
# # #         elif ls[i] == 2:
# # #             print(f"{i} is repeating")
# #
# #
# # # A = [4, 3, 6, 2, 1, 1]
# # # foo(A)
# # #
# #
# #
# # # try:
# # # 	print("Outer loop")
# # # 	try:
# # # 		print(100/0)
# # # 	except:
# # # 		# print(100/0)
# # # 		print("Error")
# # # except:
# # # 	print("outer Error")
# #
# # # a = [1,2,3,4]
# #
# # # A = [1, 3, 3, 4, 7]
# # # B = [4, 5]
# # #
# # # def foo(A, B):
# # #     n = float(len(A) + len(B))
# # #     limit = len(A) + len(B)
# # #     while (n >= 1):
# # #         import math
# # #         res = int(math.ceil(n / 2))
# # #         pointer1 = 0
# # #         pointer2 = res
# # #         while (pointer2 < limit):
# # #             if pointer1 > len(A) - 1:
# # #                 pointer4 = pointer1 - len(A)
# # #                 pointer3 = pointer2 - len(A)
# # #                 if B[pointer4] > B[pointer3]:
# # #                     B[pointer4], B[pointer3] = B[pointer3], B[pointer4]
# # #                 pointer1 += 1
# # #                 pointer2 += 1
# # #
# # #             elif pointer2 > len(A) - 1:
# # #                 pointer3 = pointer2 - len(A)
# # #                 if A[pointer1] > B[pointer3]:
# # #                     A[pointer1], B[pointer3] = B[pointer3], A[pointer1]
# # #                 pointer1 += 1
# # #                 pointer2 += 1
# # #             else:
# # #                 if A[pointer1] > A[pointer2]:
# # #                     A[pointer1], A[pointer2] = A[pointer2], A[pointer1]
# # #                 pointer1 += 1
# # #                 pointer2 += 1
# # #         n = res
# # #     return A + B
# # #
# # # print(foo(A, B))
# # #
# #
# # """
# # 1.  Higher order func - passing func arguement as arguement
# # 2. First class func - func in fun
# # 3. Closure --
# # 4. LEGB rule
# #
# # """
# #
# #
# # def deco(func):
# #     def wrapper_func():
# #         print("Good morning")
# #         print(func())
# #         print("Good evening")
# #     return wrapper_func
# #
# # @deco
# # def foo():
# #     return "Ajay"
# #
# # foo()
#
# # A= [1,2,3,4,5]
# # def foo(A):
# #     ls = []
# #     sum2 = -float('inf')
# #     for i in range(len(A)):
# #         sum1 = 0
# #         for j in range(i,len(A)):
# #             sum1 = sum1 + A[j]
# #         ls.append(sum1)
# #         sum2 = max(sum1,sum2)
# #     return sum2
# #
# # print(foo(A))
#
#
# def bitwise_or_for_all_subarray(A):
#     sum = 0
#     count = 0
#     for i in A:
#         if i == 0:
#             count = count + 1
#         else:
#             sum = sum + (count * (count + 1)) / 2
#             count = 0
#     sum = sum + (count * (count + 1)) / 2
#     n = len(A)
#     total_sum = n * (n + 1) / 2
#     return total_sum - sum, total_sum
#
#
# A = [0, 1, 0]
# print(bitwise_or_for_all_subarray(A))

# def generateNthRow(N):
#     # nC0 = 1
#     prev = 1
#     ls = [1]
#
#     for i in range(1, N + 1):
#         # nCr = (nCr-1 * (n - r + 1))/r
#         curr = (prev * (N - i + 1)) // i
#         ls.append(curr)
#         prev = curr
#     return ls
#
#
# # Driver code
# N = 5
#
# # Function calling
# print(generateNthRow(N))

# print('Ajay')
# while(True):
#     raise SystemExit('Please stop')
#
# print('Shetty')

from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')

@app.task
def hello():
    return 'hello world'

print(hello())

