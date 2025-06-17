"""Module that implements Kruskal's algorithm using existing Graph structure."""

from tools.api.graph import Graph
from tools.api.object import Vertex, Edge

class KruskalSearch(Graph):
    """A class to perform Kruskal search on a graph"""

    def __init__(self):
        super().__init__()
        self.__trees: list[set[Edge]] = []

    def __repr__(self) -> str:
        return "KruskalSearch:\n" + super().__repr__()

    def __get_tree(self, vertex: Vertex) -> set[Edge] | None:
        """Gets a tree in which a vertex is included."""
        for tree in self.__trees:
            for edge in tree:
                if vertex in [edge.get_source(), edge.get_destination()]:
                    return tree

        return None

    def run(self):
        """Performs Kruskal search on graph."""
        vertices: list[Vertex] = self.get_vertices()
        all_edges: list[Edge] = []

        for vertex in vertices:
            all_edges.extend(vertex.get_edges())

        all_edges.sort(key=lambda edge: edge.get_weight())

        for edge in all_edges:
            source = edge.get_source()
            destination = edge.get_destination()

            source_tree = self.__get_tree(source)
            destination_tree = self.__get_tree(destination)

            if source_tree is None and destination_tree is None:
                self.__trees.append(set([edge]))

            elif source_tree and destination_tree is None:
                self.__trees.append(source_tree.union([edge]))
                self.__trees.remove(source_tree)

            elif source_tree is None and destination_tree:
                self.__trees.append(destination_tree.union([edge]))
                self.__trees.remove(destination_tree)

            elif source_tree and destination_tree:
                if source_tree == destination_tree:
                    continue

                self.__trees.append(source_tree.union([edge]).union(destination_tree))
                self.__trees.remove(source_tree)
                self.__trees.remove(destination_tree)

    def get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self._get_vertices()

    def get_trees(self) -> list[set[Edge]]:
        """Returns the established MST in the graph."""
        return self.__trees
