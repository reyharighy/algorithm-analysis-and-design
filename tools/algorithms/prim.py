"""Module implementing Prim's algorithm for finding the minimum spanning tree of a graph."""

from tools.api.graph import Graph
from tools.api.object import Vertex, Edge

class PrimSearch(Graph):
    """A class to perform Prim search on a graph"""

    def __init__(self):
        super().__init__()
        self.__trees: set[Edge] = set()

    def __repr__(self) -> str:
        return "PrimSearch:\n" + super().__repr__()

    def run(self, start: Vertex):
        """Performs Prim search on graph."""
        vertices: list[Vertex] = self.get_vertices()
        visited: list[Vertex] = []
        edges_to_visit: list[Edge] = []

        visited.append(start)

        for edge in start.get_edges():
            edges_to_visit.append(edge)

        while len(vertices) != len(visited):
            edges_to_visit.sort(key=lambda edge: edge.get_weight())
            min_edge = edges_to_visit.pop(0)

            if min_edge.get_destination() in visited:
                continue

            self.__trees.add(min_edge)
            source: Vertex = min_edge.get_source()
            destination: Vertex = min_edge.get_destination()

            if source not in visited:
                visited.append(source)

            if destination not in visited:
                visited.append(destination)

            for edge in visited[-1].get_edges():
                if edge.get_destination() not in visited:
                    edges_to_visit.append(edge)

    def get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self._get_vertices()

    def get_trees(self) -> list[set[Edge]]:
        """Returns the established MST in the graph."""
        return [self.__trees]
