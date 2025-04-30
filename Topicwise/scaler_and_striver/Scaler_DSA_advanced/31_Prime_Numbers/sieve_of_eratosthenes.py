import math


def prime_number_till_n(n):
    if n == 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, math.isqrt(n)):
        if is_prime[i]:
            for x in range(i * i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]


print(prime_number_till_n(100))