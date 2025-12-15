# Undirected weighted graph
# shortest distance with minimum weight

# Problem Description
# Given a weighted undirected graph having A nodes (numbered from 0 to A-1) and M edges given in matrix B of size M x 3 where B[i][0] and B[i][1] represents the nodes connected by an edge and B[i][2] represents the weight of the edge.
# You need to find the shortest distance from the source node C to all other nodes in the graph. If some node is not reachable from the source node, then the distance to that node is -1.      
# Return an array of size A where the ith element in the array will represent the shortest distance from the source node C to node i.



class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        graph = [[] for _ in range(A)]

        # Build adjacency list: graph[u].append((v, weight))
        for u, v, w in B:
            graph[u].append((v, w))
            graph[v].append((u, w))

        distance = [float("inf") for _ in range(A)]

        from heapq import heapify, heappush, heappop
        heap = []
        heapify(heap)

        heappush(heap, (0, C))
        distance[C] = 0
        while heap:
            cur_dist, cur_node = heappop(heap)

            if cur_dist == distance[cur_node]:          # outdated heap entries are ignored
                for neighbor, weight in graph[cur_node]:
                    if distance[cur_node] + weight < distance[neighbor]:
                        distance[neighbor] = distance[cur_node] + weight
                        heappush(heap, (distance[neighbor], neighbor))
        for i in range(len(distance)):
            if distance[i] == float("inf"):
                distance[i] = -1

        return distance

    if __name__ == "__main__": 
        obj = Solution()
        A = 6
    B =[
        [0, 4, 9],
        [3, 4, 6],
        [1, 2, 1],
        [2, 5, 1],
        [2, 4, 5],
        [0, 3, 7],
        [0, 1, 1],
        [4, 5, 7],
        [0, 5, 1]
    ]
    C= 4
print(obj.solve(A, B, C))
