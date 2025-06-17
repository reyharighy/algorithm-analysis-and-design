"""A module to perform depth-first search on a graph."""

from tools.api.graph import Graph
from tools.api.object import Vertex

class DepthFirstSearch(Graph):
    """A class to perform depth-first search on a graph."""

    def __init__(self):
        super().__init__()
        self.__time = 0

    def __repr__(self) -> str:
        return "DepthFirstSearch:\n" + super().__repr__()

    def run(self, start: Vertex):
        """Performs depth-first search starting from the given vertex label."""
        self._reset('dfs')
        self.__dfs_visit(start)

    def __dfs_visit(self, vertex: Vertex):
        """Visits a vertex and explores its neighbors recursively."""
        self.__time += 1

        vertex.update_dfs_attributes(color="red", discovery_time=self.__time)

        if len(vertex.get_edges()) < 1:
            self.__update_isolated_vertices(vertex)
            return

        for edge in vertex.get_edges():
            if edge.get_destination().get_color() == 'white':
                edge.update_dfs_attributes(classification='T')
                edge.get_destination().update_dfs_attributes(predecessor=vertex)
                self.__dfs_visit(edge.get_destination())

            elif edge.get_destination().get_color() == 'red':
                edge.update_dfs_attributes(classification='B')

            elif edge.get_destination().get_color() == 'blue':
                source_time = vertex.get_discovery_time()
                destination_time = edge.get_destination().get_discovery_time()

                if source_time < destination_time:
                    edge.update_dfs_attributes(classification='F')
                else:
                    edge.update_dfs_attributes(classification='C')

        self.__update_isolated_vertices(vertex)

    def __update_isolated_vertices(self, vertex: Vertex):
        """Updates the attributes of isolated vertices."""
        self.__time += 1
        vertex.update_dfs_attributes(color='blue', finish_time=self.__time)

    def get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self._get_vertices()
