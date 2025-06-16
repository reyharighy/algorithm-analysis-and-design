"""Module that implements Kruskal's algorithm using existing Graph structure."""

from tools.api.graph import Graph
from tools.api.object import Vertex, Edge

class KruskalSearch(Graph):
    """A class to perform Kruskal search on a graph"""

    def __init__(self):
        super().__init__()
        self.__sorting_edges: list[Edge] = []

    def __repr__(self) -> str:
        return "KruskalSearch:\n" + super().__repr__()

    def run(self, start: Vertex):
        """Performs Dijkstra search starting from the given vertex label."""

    def get_vertices(self):
        """Returns the list of vertices in the graph."""
        return self._get_vertices()
# from tools.api.graph import Graph
# from tools.api.object import Edge, Vertex

# class UnionFind:
#     """A helper class for the disjoint set union (DSU) data structure."""
#     def __init__(self, vertices: list[Vertex]):
#         """Initializes the predecessor and rank for each vertex."""
#         self.predecessor = {v.get_label(): v.get_label() for v in vertices}
#         self.rank = {v.get_label(): 0 for v in vertices}

#     def find(self, label: str) -> str:
#         """Finds the root of the set containing the label with path compression."""
#         if self.predecessor[label] != label:
#             self.predecessor[label] = self.find(self.predecessor[label])
#         return self.predecessor[label]

#     def union(self, u: str, v: str):
#         """Unites the sets containing u and v using union by rank."""
#         root_u = self.find(u)
#         root_v = self.find(v)

#         if root_u != root_v:
#             if self.rank[root_u] > self.rank[root_v]:
#                 self.predecessor[root_v] = root_u
#             elif self.rank[root_u] < self.rank[root_v]:
#                 self.predecessor[root_u] = root_v
#             else:
#                 self.predecessor[root_v] = root_u
#                 self.rank[root_u] += 1

# def kruskal(graph: Graph) -> list[Edge]:
#     mst_edges: list[Edge] = []

#     all_edges: list[Edge] = []
#     for vertex in graph._get_vertices():
#         all_edges.extend(vertex.get_edges())

#     # Sort all edges by weight in ascending order
#     all_edges.sort(key=lambda e: e.get_weight())

#     # Initialize Union-Find structure
#     uf = UnionFind(graph._get_vertices())

#     # Iterate through sorted edges and add to MST if they don't form a cycle
#     for edge in all_edges:
#         source_label = edge.get_source().get_label()
#         dest_label = edge.get_destination().get_label()

#         if uf.find(source_label) != uf.find(dest_label):
#             mst_edges.append(edge)
#             uf.union(source_label, dest_label)

#     return mst_edges
