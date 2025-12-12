

from collections import deque


class Solution:
    def solve(self, A, B):
        """Check if the undirected graph with A nodes and edge list B is bipartite.

        Returns 1 if bipartite, else 0.
        """
        graph = [[] for _ in range(A)]
        for edge in B:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        color = [0] * A  # 0 = unvisited, 1 and 2 are two colours
        q = deque()

        for node in range(A):
            # start BFS from this connected component
            if color[node] == 0:
                q.append(node)
                color[node] = 1 # colour with 1
            
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if color[v] == 0:
                        # color with opposite colour (1 <-> 2)
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        # adjacent nodes have same colour -> not bipartite
                        return 0
        return 1

if __name__ == "__main__":
    A = 94
    B = [
      [10, 82],
      [43, 64],
      [24, 56],
      [35, 66],
      [44, 70],
      [7, 27],
      [29, 82],
      [1, 86],
      [5, 27],
      [68, 82],
      [5, 41],
      [36, 64],
      [0, 38],
      [30, 92],
      [51, 88],
      [12, 52],
      [45, 59],
      [40, 41],
      [17, 28],
      [43, 46],
      [22, 62],
      [17, 25],
      [38, 91],
      [44, 74],
      [26, 57],
      [27, 88],
      [57, 68],
      [19, 76],
      [63, 85],
      [32, 36],
      [3, 50],
      [42, 71],
      [44, 75],
      [56, 92],
      [23, 47],
      [40, 93],
      [56, 59],
      [24, 51],
      [46, 68],
      [32, 90],
      [25, 37],
      [26, 92],
      [3, 9],
      [76, 90],
      [68, 93],
      [34, 48],
      [53, 71],
      [15, 79],
      [10, 37],
      [13, 66],
      [66, 79],
      [17, 26],
      [3, 41],
      [45, 57],
      [73, 92],
      [14, 28],
      [67, 92],
      [33, 39],
      [25, 63],
      [20, 71],
      [22, 29],
      [33, 49],
      [9, 41],
      [26, 80],
]
    obj = Solution()
    print(obj.solve(A, B))
