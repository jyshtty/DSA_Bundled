A = [5, 17, 100, 11]
B = [1]

def left_rotation(A,B):
    lis = []
    n = len(A)
    for i in B:
        C = A[::-1]
        i = i%n
        k = n-i
        lis.append((C[0:k])[::-1] + (C[k:])[::-1])
    return lis

print(left_rotation(A,B))

#   [ [3, 4, 5, 1, 2]
#      [4, 5, 1, 2, 3] ]

