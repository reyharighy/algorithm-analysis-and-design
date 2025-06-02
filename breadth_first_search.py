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

    def __reset(self):
        """Resets the graph's vertices to their initial state."""
        for vertex in self._vertices:
            vertex.update_attributes(
                predecessor=None,
                distance=float('inf'),
                visited=False,
                color='white'
            )

    def get_vertices(self) -> list['Vertex']:
        """Returns the list of vertices in the graph."""
        return self._vertices

    @validate_labels('start_label')
    def run(self, start_label: str):
        """Performs breadth-first search starting from the given vertex label."""
        start_vertex = self._get_vertex(start_label)

        if start_vertex is None:
            raise ValueError(f"Vertex with label '{start_label}' does not exist.")

        self.__reset()

        start_vertex.update_attributes(
            distance=0,
            visited=True,
            color='red'
        )

        self.__queue.append(start_vertex)

        while self.__queue:
            head = self.__queue.popleft()

            for neighbor in head.get_neighbors():
                if neighbor.get_color() == 'white':
                    neighbor.update_attributes(
                        predecessor=head,
                        distance= head.get_distance() + 1,
                        visited=True,
                        color='red'
                    )

                    self.__queue.append(neighbor)

            head.update_attributes(color='blue')
