"""
Find maximum sum of a subarray in O(N)
"""

A = [-2,-3,4,-1,-2,1,5,-3]
def foo(A):
    sum_ = 0
    maxi = -float('inf')
    for x in A:
        sum_ = max(x, sum_ + x)   # Either start new subarray at x or extend
        maxi = max(maxi, sum_)
    return maxi

print(foo(A))


# import  protgres
#
# connection = protgres.connect('connection'string)
#
# mbr = conection.excute('select * from mbr')
