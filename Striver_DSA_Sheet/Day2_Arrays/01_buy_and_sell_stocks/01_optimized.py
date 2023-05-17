def foo(A):
    mini = A[0]
    max_profit = 0
    for i in range(1, len(A)):
        if A[i] < mini:
            mini = A[i]
        else:
            max_profit = max(max_profit, (A[i] - mini))
    return max_profit

A = [7,1,5,3,6,4]
print(foo(A))


