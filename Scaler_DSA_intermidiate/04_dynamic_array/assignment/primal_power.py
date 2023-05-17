"""
"Primal Power" of an array is defined as the count of prime numbers present in it.

Given an array of integers A of length N, you have to calculate its Primal Power.
"""
def isPrime(n, count):
    if n == 0 or n == 1:
        return count
    if n == 2:
        count +=1
        return count
    i = 2
    while(i*i <= n):
        if n%i == 0:
            return count
        i = i + 1
    count += 1
    return count

def solve(A):
    count = 0
    for i in A:
        count = isPrime(i, count)
    return count

print(solve([1,2,3,4,5,6,7,10,]))


