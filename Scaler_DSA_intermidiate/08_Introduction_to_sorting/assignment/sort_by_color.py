def sort_by_color(A):
    count_0 = count_1 = count_2 = 0
    for i in A:
        if i == 0:
            count_0 +=1
        elif i == 1:
            count_1 +=1
        else:
            count_2 +=1
    return [0] * count_0 + [1] * count_1 + [2] * count_2

A = [0]

print(sort_by_color(A))



