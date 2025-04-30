A = [1, 3, 3, 4, 7]
B = [4, 5]

def foo(A, B):
    n = float(len(A) + len(B))
    limit = len(A) + len(B)
    while (n >= 1):
        import math
        res = int(math.ceil(n / 2))
        pointer1 = 0
        pointer2 = res
        while (pointer2 < limit):
            if pointer1 > len(A) - 1:
                pointer4 = pointer1 - len(A)
                pointer3 = pointer2 - len(A)
                if B[pointer4] > B[pointer3]:
                    B[pointer4], B[pointer3] = B[pointer3], B[pointer4]
                pointer1 += 1
                pointer2 += 1
            elif pointer2 > len(A) - 1:
                pointer3 = pointer2 - len(A)
                if A[pointer1] > B[pointer3]:
                    A[pointer1], B[pointer3] = B[pointer3], A[pointer1]
                pointer1 += 1
                pointer2 += 1
            else:
                if A[pointer1] > A[pointer2]:
                    A[pointer1], A[pointer2] = A[pointer2], A[pointer1]
                pointer1 += 1
                pointer2 += 1
        n = res
    return A + B

print(foo(A, B))