"""Module that implements Kruskal's algorithm using existing Graph structure."""
from graph import Graph
from object import Edge, Vertex

class UnionFind:
    def __init__(self, vertices: list[Vertex]):
        # Initialize parent and rank for union-find structure
        self.parent = {v.get_label(): v.get_label() for v in vertices}
        self.rank = {v.get_label(): 0 for v in vertices}  # Gunakan rank untuk optimasi union

    def find(self, label: str) -> str:
        # Find the root of the set containing the label
        if self.parent[label] != label:
            self.parent[label] = self.find(self.parent[label])  # Path compression
        return self.parent[label]

    def union(self, u: str, v: str):
        # Union the sets containing u and v
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return

        # Union by rank
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

def kruskal(graph: Graph) -> list[Edge]:
    # Get all edges from the graph and sort them by weight
    edges = graph._get_edges()
    edges.sort(key=lambda e: e.get_weight())  # Sort edges by weight ascending
    uf = UnionFind(graph._get_vertices())

    mst_edges: list[Edge] = []

    for edge in edges:
        u = edge.get_source().get_label()
        v = edge.get_destination().get_label()

        if uf.find(u) != uf.find(v):
            mst_edges.append(edge)
            uf.union(u, v)

    return mst_edges