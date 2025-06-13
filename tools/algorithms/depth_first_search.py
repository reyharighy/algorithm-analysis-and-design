"""A module to perform depth-first search on a graph."""

from tools.api.graph import Graph
from tools.api.object import Vertex
from helper.validators import validate_labels

class DepthFirstSearch(Graph):
    """A class to perform depth-first search on a graph."""

    def __init__(self):
        super().__init__()
        self.__time = 0

    def __repr__(self) -> str:
        return "DepthFirstSearch:\n" + super().__repr__()

    @validate_labels('start_label')
    def run(self, start_label: str):
        """Performs depth-first search starting from the given vertex label."""
        start_vertex = self._get_vertex(start_label)

        if start_vertex is None:
            raise ValueError(f"Vertex with label '{start_label}' does not exist.")

        self._reset('dfs')

        for vertex in self._get_vertices():
            if vertex.get_color() == 'white':
                self.__dfs_visit(vertex)

    def __dfs_visit(self, vertex: Vertex):
        """Visits a vertex and explores its neighbors recursively."""
        self.__time += 1

        vertex.update_default_attributes(color='red')
        vertex.update_dfs_attributes(discovery_time=self.__time)

        neighbors = vertex.get_neighbors()

        if neighbors is None:
            self.__update_isolated_vertices(vertex)
            return

        for neighbor in neighbors:
            if neighbor.get_color() == 'white':
                neighbor.update_default_attributes(predecessor=vertex)
                self.__dfs_visit(neighbor)

        self.__update_isolated_vertices(vertex)

    def __update_isolated_vertices(self, vertex: Vertex):
        """Updates the attributes of isolated vertices."""
        self.__time += 1

        vertex.update_default_attributes(color='blue')
        vertex.update_dfs_attributes(finish_time=self.__time)

    # omit for later use
    def get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self._get_vertices()
