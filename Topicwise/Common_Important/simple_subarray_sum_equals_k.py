def subarray_sum(arr, k):

    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]

    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]   # corrected

    hm = {0: -1}   # important for subarray starting from index 0

    for i in range(len(arr)):

        if prefix_sum[i] - k in hm:   # corrected condition
            start = hm[prefix_sum[i] - k] + 1
            return arr[start:i+1]

        hm[prefix_sum[i]] = i

    return None
