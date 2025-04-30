def solve(A):
    # create hash map
    dict01 = dict(zip(A, A))
    n = len(A)

    if len(dict01) != len(A):
        return 0

    # find first min and second min
    first_min = float('inf')
    second_min = float('inf')
    # import pdb; pdb.set_trace()
    for i in A:
        if i < first_min:
            second_min = first_min
            first_min = i
        elif (i < second_min and i != first_min):
            second_min = i

    d = second_min - first_min

    # last elem
    last_elem = first_min + (n - 1) * d

    if last_elem not in dict01:
        return 0

    new_element = second_min
    # import pdb;
    # pdb.set_trace()

    while (new_element < last_elem):
        new_element += d
        if new_element not in dict01:
            return 0
        else:
            continue

    return 1

A = [ -97, -79, -88, -43, -61, -106, -52, -151, -115, -34, -142, -16, -124, -133, -25, -70 ]
print(solve(A))
