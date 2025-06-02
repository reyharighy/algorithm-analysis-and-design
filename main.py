"""Main module to run the graph operations."""
from breadth_first_search import BreadthFirstSearch

bfs = BreadthFirstSearch()

for i in range(65, 75):
    bfs.add_vertex(chr(i))

edge_dictionary = {
    'A': ['B', 'D', 'E'],
    'B': ['C'],
    'C': ['G', 'H'],
    'D': ['F'],
    'E': ['D', 'F'],
    'F': ['J'],
    'G': [],
    'H': ['G'],
    'I': ['G', 'H'],
    'J': [],
}

for source, dest in edge_dictionary.items():
    for d in dest:
        bfs.add_edge(source, d)

print(bfs)
