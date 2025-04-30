arr = [2,3,4,5,7,6, float('inf')]
x = 4

def partition(arr ,l,h):
    i = l
    j = h
    while i < j:
        i += 1
        while arr[i] < arr[l] and i <= h:
            i += 1
        j -= 1
        if j<i:
            arr[l], arr[j] = arr[j], arr[l]
            return j
        while arr[j] > arr[l] and j >= l:
            j -= 1
        if j<i:
            arr[l], arr[j] = arr[j], arr[l]
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr,l,h):
    if l < h:
        j = partition(arr , l,h)

        quick_sort(arr, l, j-1)
        quick_sort(arr, j+1, h)


quick_sort(arr, 0, len(arr)-1)
print(arr)

# j >> 3 >> 1  >> 0





