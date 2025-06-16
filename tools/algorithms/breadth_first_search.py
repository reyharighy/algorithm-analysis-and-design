"""A module to perform breadth-first search on a graph."""

from collections import deque
from tools.api.graph import Graph
from tools.api.object import Vertex

class BreadthFirstSearch(Graph):
    """A class to perform breadth-first search on a graph."""

    def __init__(self):
        super().__init__()
        self.__queue: deque['Vertex'] = deque()

    def run(self, start: Vertex):
        """Performs breadth-first search starting from the given vertex label."""
        self._reset('bfs')

        start.update_bfs_attributes(color="red", distance=0)

        self.__queue.append(start)

        while self.__queue:
            head = self.__queue.popleft()

            for edge in head.get_edges():
                if edge.get_destination().get_color() == 'white':
                    edge.get_destination().update_bfs_attributes(
                        color='red',
                        predecessor=head,
                        distance=head.get_distance() + 1
                    )

                    self.__queue.append(edge.get_destination())

            head.update_bfs_attributes(color='blue')

    def get_vertices(self):
        """Returns the list of vertices in the graph."""
        return self._get_vertices()
