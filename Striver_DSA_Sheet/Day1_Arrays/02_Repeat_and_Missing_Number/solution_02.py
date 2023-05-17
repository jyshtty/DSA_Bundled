def foo(A):
    n = len(A)
    prefix_even = [0] * n
    prefix_odd = [0] * n
    for i in range(n):
        if i % 2 == 0:
            prefix_even[i] = prefix_even[i-1] + A[i]
            prefix_odd[i] = prefix_odd[i-1]
        else:
            prefix_odd[i] = prefix_odd[i-1] + A[i]
            prefix_even[i] = prefix_even[i-1]
    return prefix_even, prefix_odd

A = [4,3,6,2,1]
print(foo(A))