# https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/
# Given a matrix of dimension m*n where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
# 0: Empty cell
# 1: Cells have fresh oranges
# 2: Cells have rotten oranges
# We have to determine what is the minimum time required so that all oranges become rotten. A rotten orange at index [i,j] can rot other fresh orange at indexes
# [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 
# If it is impossible to rot every orange then simply return -1.

# We can use multi-source BFS here. First, we will insert all the rotten oranges in the queue. Now, we will run BFS and for each rotten orange, we will rot its adjacent fresh oranges and insert them into the queue. We will also keep a time counter which will be incremented each time we finish processing all the oranges at the current time level. Finally, we will check if all oranges are rotten or not. If yes, we will return the time counter else -1.


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        total = 0
        rotten = 0
        from collections import deque
        q = deque()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1 or A[i][j] == 2:
                    total += 1
                if A[i][j] == 2:
                    rotten += 1
                    q.append([i,j])

        l = len(A)
        b = len(A[0])
        time = 0
        q.append([100,100])
        while q and len(q) > 1:
            x,y = q.popleft()
            if x == 100 and y == 100:
                time += 1
                if q: # very important to check if q is not empty before appending the level delimiter. otherwise infinite loop.
                    q.append([100, 100])
                continue
            if x>0 and A[x-1][y] == 1:
                A[x-1][y] = 2
                rotten += 1
                q.append([x-1, y])
            if y >0 and A[x][y-1] == 1:
                A[x][y-1] = 2
                rotten += 1
                q.append([x, y-1])
            if x < l - 1 and A[x+1][y] == 1:
                A[x+1][y] = 2
                rotten += 1
                q.append([x+1, y])
            if y < b - 1 and A[x][y+1] == 1:
                A[x][y+1] = 2
                rotten += 1
                q.append([x, y+1])

        if total == rotten:
            return time
        return -1

if __name__ == "__main__":
    A = [[2, 1, 1],
         [1, 1, 0],
         [0, 1, 1]]
    obj = Solution()
    print(obj.solve(A))
