"""Main module to run the graph operations."""

from breadth_first_search import BreadthFirstSearch

bfs = BreadthFirstSearch()
bfs.create_graph_from_problem_statement()

for vertex in bfs.get_vertices():
    print(vertex)

bfs.run('A')

print('')
for vertex in bfs.get_vertices():
    print(vertex)
