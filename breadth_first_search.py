"""A module to perform breadth-first search on a graph."""

from collections import deque
from graph import Graph
from object import Vertex
from validators import validate_labels

class BreadthFirstSearch(Graph):
    """A class to perform breadth-first search on a graph."""

    def __init__(self):
        super().__init__()
        self.__queue: deque['Vertex'] = deque()

    def __repr__(self) -> str:
        """Returns a string representation of the graph."""
        return "BreadthFirstSearch:\n" + super().__repr__()

    @validate_labels('start_label')
    def run(self, start_label: str):
        """Performs breadth-first search starting from the given vertex label."""
        start_vertex = self._get_vertex(start_label)

        if start_vertex is None:
            raise ValueError(f"Vertex with label '{start_label}' does not exist.")

        self._reset('bfs')

        start_vertex.update_default_attributes(color='red')
        start_vertex.update_bfs_attributes(distance=0)

        self.__queue.append(start_vertex)

        while self.__queue:
            head = self.__queue.popleft()

            for neighbor in head.get_neighbors():
                if neighbor.get_color() == 'white':
                    neighbor.update_default_attributes(color='red', predecessor=head)
                    neighbor.update_bfs_attributes(distance=head.get_distance() + 1)
                    self.__queue.append(neighbor)

            head.update_default_attributes(color='blue')

    # omit for later use
    def get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self._get_vertices()
