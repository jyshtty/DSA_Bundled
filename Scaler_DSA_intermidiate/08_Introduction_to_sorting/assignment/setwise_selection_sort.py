"""
Explanation : 6 4 3 7 2 8 : Index of 1st min - 4
 After 1st Iteration : 2 4 3 7 6 8 : Index of 2nd min - 2
 After 2nd Iteration : 2 3 4 7 6 8 : Index of 3rd min - 2
 After 3rd Iteration : 2 3 4 7 6 8 : Index of 4th min - 4
 After 4th iteration : 2 3 4 6 7 8 : Index of 5th min - 4
 After 5th iteration. : 2 3 4 6 7 8.
"""
#     [4, 2, 3, 3, 4, 5], [2, 3, 7, 8, 8, 8]
def solve(A):
    arr = []
    for i in range(len(A)-1):
        mini = i
        for j in range(i+1,len(A)-1):
            if A[mini] > A[j]:
                mini = j
        A[i],A[mini] = A[mini],A[i]
        # import pdb;pdb.set_trace()
        arr.append(mini)
        if i == 3:
            import pdb; pdb.set_trace()

    return A,arr

A = [6, 4, 3, 7, 2, 8]
print(solve(A))



