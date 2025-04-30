A = [1, 3, 3, 4, 7]
B = [4, 5]

def foo1(A, B):
    for i in range(len(A)):
        j = 0
        while (j < len(B)):
            if A[i] <= B[j]:
                j += 1
                continue
            else:
                A[i], B[j] = B[j], A[i]
                B.sort()
    return A + B

def foo2(A, B):
    j = 0
    i = 0
    while i < len(A):
        if A[i] > B[j]:
            temp = B[j]
            B[j] = A[i]
            A[i] = temp
            B.sort()
        i += 1
    return A + B

print(foo1(A, B))
