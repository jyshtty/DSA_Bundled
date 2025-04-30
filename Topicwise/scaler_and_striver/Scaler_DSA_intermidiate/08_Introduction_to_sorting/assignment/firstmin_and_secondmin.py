# Python program to find smallest and second smallest elements
import sys


def print2Smallest(arr):
    # There should be atleast two elements
    arr_size = len(arr)

    first = second = sys.maxint
    for i in arr:

        # If current element is smaller than first then
        # update both first and second
        if i < first:
            second = first
            first = i

        # If arr[i] is in between first and second then
        # update second
        elif (i < second and i != first):
            second = i;

    if (second == sys.maxint):
        print "No second smallest element"
    else:
        print 'The smallest element is', first, 'and' \
                                                ' second smallest element is', second


# Driver function to test above function
arr = [ -97, -79, -88, -43, -61, -106, -52, -151, -115, -34, -142, -16, -124, -133, -25, -70 ]
print2Smallest(arr)