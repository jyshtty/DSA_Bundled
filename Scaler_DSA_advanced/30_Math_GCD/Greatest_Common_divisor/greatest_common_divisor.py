def gcd(A,B):
    if B == 0:
        return A
    return gcd(B,A%B)


print(gcd(6,7))