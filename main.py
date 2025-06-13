"""Main module to run the graph operations."""

from tools.algorithms.breadth_first_search import BreadthFirstSearch
from tools.algorithms.depth_first_search import DepthFirstSearch
from tools.algorithms.dijkstra import DijkstraSearch
from tools.api.graph import Graph
from tools.algorithms.prim import prim
from tools.algorithms.kruskal import kruskal

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

# -------------------------------------------------------------------------------
# --- Prim's Algorithm (Task 2) ---
# -------------------------------------------------------------------------------
print("\n--- Prim's Algorithm (Task 2) ---")
prim_graph = Graph()
# Pastikan __create_graph_task_2 sudah ditambahkan ke `graph.py`
prim_graph.create_graph_from_problem_statement(2)

print("Running Prim's algorithm to find MST...\n")
mst_prim = prim(prim_graph, start_label='A')

total_weight_prim = 0
print("Edges in MST (Prim):")
for edge in mst_prim:
    print(f"- {edge}")
    total_weight_prim += edge.get_weight()

print(f"\nTotal weight of MST (Prim): {total_weight_prim}")
print("-" * 50)


# -------------------------------------------------------------------------------
# --- Kruskal's Algorithm (Task 2) ---
# -------------------------------------------------------------------------------
print("\n--- Kruskal's Algorithm (Task 2) ---")
kruskal_graph = Graph()
# Pastikan __create_graph_task_2 sudah ditambahkan ke `graph.py`
kruskal_graph.create_graph_from_problem_statement(2)

print("Running Kruskal's algorithm to find MST...\n")
mst_kruskal = kruskal(kruskal_graph)

total_weight_kruskal = 0
print("Edges in MST (Kruskal):")
for edge in mst_kruskal:
    print(f"- {edge}")
    total_weight_kruskal += edge.get_weight()

print(f"\nTotal weight of MST (Kruskal): {total_weight_kruskal}")
print("-" * 50)