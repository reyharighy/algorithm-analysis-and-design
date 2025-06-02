"""A module to perform breadth-first search on a graph."""
from graph import Graph
from object import Vertex
from validators import validate_labels

class BreadthFirstSearch(Graph):
    """A class to perform breadth-first search on a graph."""

    def __repr__(self) -> str:
        """Returns a string representation of the graph."""
        return "BreadthFirstSearch:\n" + super().__repr__()

    @validate_labels('vertex_label')
    def get_neighbors(self, vertex_label: str) -> list[Vertex]:
        """Returns a list of neighboring vertices for the given vertex label."""
        vertex = self.get_vertex(vertex_label)

        if vertex is None:
            return []

        return [edge.destination for edge in vertex.edges]
