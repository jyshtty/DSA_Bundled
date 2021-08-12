"""
Find maximum sum of a subarray in O(N)
"""

# A = [-2,-3,4,-1,-2,1,5,-3]
# def foo(A):
#     sum = 0
#     maxi = -float('inf')
#     for i in range(len(A)):
#         if A[i] + sum < 0:
#             sum = 0
#         else:
#             sum = sum + A[i]
#         maxi = max(sum, maxi)
#     return maxi
#
# print(foo(A))


# import  protgres
#
# connection = protgres.connect('connection'string)
#
# mbr = conection.excute('select * from mbr')