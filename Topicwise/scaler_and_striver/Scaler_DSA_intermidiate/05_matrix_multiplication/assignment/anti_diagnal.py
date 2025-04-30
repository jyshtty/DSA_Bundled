def diagonal(A):
    N = 3
    total = []
    # For each column start row is 0
    for col in range(N):

        startcol = col
        startrow = 0
        new_list = []
        while (startcol >= 0 and startrow < N):
            new_list.append(A[startrow][startcol])

            startcol -= 1
            startrow += 1
        total.append(new_list)
    # For each row start column is N-1
    for row in range(1, N):
        startrow = row
        startcol = N - 1
        new_list = []
        while (startrow < N and startcol >= 0):
            new_list.append(A[startrow][startcol])

            startcol -= 1
            startrow += 1

        total.append(new_list)
    return total

# Driver code
if __name__ == "__main__":
    # matrix iniliasation
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    print(diagonal(A))

