def z_algo(A):
    for i in range(len(A)):
        j = 0
        temp = i
        while(i < len(A)):
            if A[i] == A[j]:
                z[temp] += 1
                i += 1
                j += 1
            else:
                break
    return z

A = "abacaba"
z = [0] * len(A)

print(z_algo(A))

