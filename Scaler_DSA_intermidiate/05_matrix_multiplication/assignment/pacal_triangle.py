def pascal_triangle(n):
    # lis = []
    # for i in range(n):
    #     c = []
    #     c = [int(j) for j in str(11**i)]
    #     lis.append(c)
    # return lis
    lis = []
    for line in range(1, n + 1):
        C = 1;  # used to represent C(line, i)
        lis01 = []
        for i in range(1, line + 1):
            # The first value in a
            # line is always 1
            lis01.append(C)
            C = int(C * (line - i) / i);
        lis.append(lis01)
    return lis

print(pascal_triangle(5))