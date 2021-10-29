# Python 3 implementation of
# doors open or closed
import math


# Function to check whether
# 'n' has even number of
# factors or not
def hasEvenNumberOfFactors(n):
    root_n = math.sqrt(n)

    # if 'n' is a perfect square
    # it has odd number of factors
    if ((root_n * root_n) == n):
        return False

    # else 'n' has even
    # number of factors
    return True


# Function to find and print
# status of each door
def printStatusOfDoors(n):
    for i in range(1, n + 1):

        # If even number of factors
        # final status is closed
        if (hasEvenNumberOfFactors(i) == True):
            print("closed", end =" ")

        # else odd number of factors
        # final status is open
        else:
            print("open", end =" ")


# Driver program
n = 5

printStatusOfDoors(n)

# This code is contributed by Smitha Dinesh Semwal