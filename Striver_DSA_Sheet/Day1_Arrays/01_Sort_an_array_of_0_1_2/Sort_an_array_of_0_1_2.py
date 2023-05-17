# def weightCapacity(weights, maxCapacity):
#     weight_comb = set([0])
#     for weight in weights:
#         temp = set()  # Store new weights comb
#
#         # For each previous weights comb,
#         for curr_sum in weight_comb:
#             if weight + curr_sum == maxCapacity:
#                 return maxCapacity
#             elif weight + curr_sum < maxCapacity:
#                 temp.add(weight + curr_sum)
#
#         weight_comb.update(temp)  # update
#
#     return max(weight_comb)
#
# print(weightCapacity(A, B))

def sort_array(A):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in A:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        else:
            count_2 += 1
    return [0]  * count_0 + [1] * count_1 + [2] * count_2

A = [2,0,2,1,1,0]
print(sort_array(A))