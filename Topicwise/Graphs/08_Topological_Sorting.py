# Directional Acyclic Graph (DAG) Topological Sorting

# Topological Sorting using Kahn's Algorithm (BFS)
# We will maintain an indegree array to keep track of the number of incoming edges for each node.
# We will use a min-heap (priority queue) to ensure that we always process the smallest numbered node available.
# We will start by adding all nodes with indegree 0 to the min-heap.
# We will then repeatedly extract the smallest node from the heap, add it to the result list, and decrease the indegree of its neighbors.
# If any neighbor's indegree becomes 0, we will add it to the min-heap.
# We will continue this process until the heap is empty.
# The result list will contain the nodes in topologically sorted order. 

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
        return ans

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
