"""Main module to run the graph operations."""

from tools.algorithms.breadth_first_search import BreadthFirstSearch
from tools.algorithms.depth_first_search import DepthFirstSearch
from tools.algorithms.dijkstra import DijkstraSearch

# Run Breadth-First Search (BFS)
bfs = BreadthFirstSearch()
bfs.create_graph_from_problem_statement(1)

print("Before BFS traversal:")
for vertex in bfs.get_vertices():
    print(vertex, end=' ')
    print(f"({{distance: {vertex.get_distance()}}})")

bfs.run('A')

print("\nAfter BFS traversal:")
for vertex in bfs.get_vertices():
    print(vertex, end=' ')
    print(f"({{distance: {vertex.get_distance()}}})")

# Run Depth-First Search (DFS)
dfs = DepthFirstSearch()
dfs.create_graph_from_problem_statement(1)

print("\nBefore DFS traversal:")
for vertex in dfs.get_vertices():
    print(vertex, end=' ')

    S = f"(discovery_time: {vertex.get_discovery_time()}, finish_time: {vertex.get_finish_time()})"

    print(S)

dfs.run('A')

print("\nAfter DFS traversal:")
for vertex in dfs.get_vertices():
    print(vertex, end=' ')

    S = f"(discovery_time: {vertex.get_discovery_time()}, finish_time: {vertex.get_finish_time()})"

    print(S)

dijkstra = DijkstraSearch()
dijkstra.create_graph_from_problem_statement(3)

print("\nBefore Dijkstra traversal:")
for vertex in dijkstra.get_vertices():
    print(vertex, end=" ")
    print(f"({{distance: {vertex.get_distance()}}})")

dijkstra.run('S')

print("\nAfter Dijkstra traversal:")
for vertex in dijkstra.get_single_source():
    print(vertex, end=" ")
    print(f"({{distance: {vertex.get_distance()}}})")
