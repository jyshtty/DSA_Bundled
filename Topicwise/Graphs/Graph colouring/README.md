# Graph Colouring — Bipartite Coloring

This folder contains solutions and discussion for graph colouring problems, focusing on checking whether a graph is bipartite (2-colourable). A graph is bipartite when its vertices can be coloured with two colours such that no two adjacent vertices share the same colour.

## Problem
Given an undirected graph, determine whether it is bipartite. Input is typically an adjacency list (list of lists) or a list of edges.

## Approaches
- BFS (level-order colouring): start from an unvisited vertex, assign a colour (0/1), and assign alternate colours to neighbours. If a neighbour already has the same colour, the graph isn't bipartite.
- DFS (recursive or iterative): same colouring idea, but using DFS traversal.

Both BFS and DFS solutions run in O(V + E) time, and require O(V) space for the colour/visited arrays.

## Example (adjacency list)
```py
# adjacency as list of lists (0-based index)
graph = [ [1, 2], [0, 3], [0, 3], [1, 2] ]  # 4-vertex even cycle -> bipartite
# call the checker: is_bipartite(graph) -> True
```

## Usage
- Inspect or run `Bipartite_Coloring_Graph.py` for an implementation. If the script includes a `main` block it can be run directly.

## Complexity
- Time: O(V + E)
- Space: O(V)

