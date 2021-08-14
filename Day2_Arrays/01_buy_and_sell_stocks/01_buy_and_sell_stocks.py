# brute force

def foo(A):
    maxi = 0
    for i in range(len(A)-1):
        for j in range(i, len(A)):
            if A[i] < A[j]:
                maxi = max(maxi, A[j] - A[i])
    return maxi
A = [7,1,5,3,6,4]
print(foo(A))