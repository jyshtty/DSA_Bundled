A = [1, 3, 3, 4, 7]
B = [4, 5]

def foo(A, B):
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

print(foo(A, B))
