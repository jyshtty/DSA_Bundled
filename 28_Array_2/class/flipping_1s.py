"""
Maximum number of 0s in an array after flipping a subarray
"""

def maximum_number_of_ones(A):
    count_of_zeros = A.count(0)
    for i in range(len(A)):
        if A[i] == 0:
            A[i] = -1
    global_max = -float('inf')
    curr_max = -float('inf')
    for i in range(len(A)):
        curr_max = max(curr_max + A[i], A[i])
        if curr_max > global_max:
            global_max = curr_max
    return count_of_zeros + global_max


A=[0,0,0,0,1,1,1,1]
print(maximum_number_of_ones(A))