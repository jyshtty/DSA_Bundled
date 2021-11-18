def foo(A):
    A.sort()
    r = 1
    ls = []
    merged_array = A[0]
    while r < len(A):
        if merged_array[1] >= A[r][0]:
            merged_array = (merged_array[0], max(merged_array[1], A[r][1]))
        else:
            ls.append(merged_array)
            merged_array = A[r]
        r = r + 1
    ls.append(merged_array)
    return ls

A = [[1,3],[2,6],[8,10],[15,18]]
print(foo(A))






