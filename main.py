"""Main module to run the graph operations."""

from breadth_first_search import BreadthFirstSearch
from depth_first_search import DepthFirstSearch
from dijkstra import Dijkstra

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

dfs = DepthFirstSearch()
dfs.create_graph_from_problem_statement(1)

print("\nBefore DFS traversal:")
for vertex in dfs.get_vertices():
    print(vertex, end=' ')

    S = "({{"
    S += f"discovery_time: {vertex.get_discovery_time()}, "
    S += f"finish_time: {vertex.get_finish_time()}"
    S += "}})"

    print(S)

dfs.run('A')

print("\nAfter DFS traversal:")
for vertex in dfs.get_vertices():
    print(vertex, end=' ')

    S = "({{"
    S += f"discovery_time: {vertex.get_discovery_time()}, "
    S += f"finish_time: {vertex.get_finish_time()}"
    S += "}})"

    print(S)

dijkstra = Dijkstra()
dijkstra.create_graph_from_problem_statement(3)
dijkstra.run('S')

print("\nAfter Dijkstra traversal:")
for vertex in dijkstra.get_vertices():
    print(vertex, f"({{distance: {vertex.get_dijkstra_distance()}}})")
    
dijkstra.visualize()