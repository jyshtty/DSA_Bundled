"""
Maximum number of 0s in an array after flipping a subarray
"""

def maximum_number_of_ones(A):
    A = [int(i) for i in A]
    count_of_ones = A.count(1)
    if count_of_ones == len(A):
        return []
    index = [-1,-1]
    for i in range(len(A)):
        if A[i] == 1:
            A[i] = -1
        else:
            A[i] = 1
    global_max = -float('inf')
    curr_max = -float('inf')
    for i in range(len(A)):
        if A[i] > curr_max + A[i]:
            index = [i+1,i+1]
            curr_max = A[i]
        else:
            curr_max = curr_max + A[i]
            index[1] = index[1] + 1
        if curr_max > global_max:
            global_index = list(index)
            global_max = curr_max
    return global_max, global_index


A='0011101'

print(maximum_number_of_ones(A))