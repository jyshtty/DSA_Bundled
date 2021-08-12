def weightCapacity(weights, maxCapacity):
    weight_comb = set([0])
    for weight in weights:
        temp = set()  # Store new weights comb

        # For each previous weights comb,
        for curr_sum in weight_comb:
            if weight + curr_sum == maxCapacity:
                return maxCapacity
            elif weight + curr_sum < maxCapacity:
                temp.add(weight + curr_sum)

        weight_comb.update(temp)  # update

    return max(weight_comb)

print(weightCapacity(A, B))