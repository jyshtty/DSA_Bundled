# Problem Description
# Given a directed graph having A nodes. The nodes are numbered from 1 to A.
# determine cycle in directed graph.


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers

    def solve(self, A, B):
        indegree = [0] * (A + 1)
        indegree[0] = float("inf")
        adj = [[] for i in range((A + 1))]
        for i in B:
            adj[i[0]].append(i[1])
            # Update the indegree of the destination node - incoming edge
            indegree[i[1]] += 1

        from collections import deque
        from heapq import heapify, heappush, heappop

        q = []
        heapify(q)

        # Push all nodes with indegree 0 into the min-heap
        for i in range(1, len(indegree)):
            if indegree[i] == 0:
                heappush(q, i)


        ans = []
        while q:
            v = heappop(q)
            # Add the node to the result list
            ans.append(v)
            for i in adj[v]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    heappush(q, i)
        if len(ans) == A:
            return True
        return False

if __name__ == "__main__":
    A = 8
    B = [ [1, 4],
  [1, 2],
  [4, 2],
  [4, 3],
  [3, 2],
  [5, 2],
  [3, 5],
  [8, 2],
  [8, 6]]
    obj = Solution()
    print(obj.solve(A, B))
    # 1 4 3 5 7 8 2 6
