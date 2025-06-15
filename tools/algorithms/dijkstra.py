"""Module that implements Dijkstra's algorithm using existing Graph structure."""

from collections import deque
from tools.api.graph import Graph
from tools.api.object import Vertex
from helper.validators import validate_labels

class DijkstraSearch(Graph):
    """A class to perform Dijkstra search on a graph"""

    def __init__(self):
        super().__init__()
        self.__single_source: list[Vertex] = []
        self.__queue: deque['Vertex'] = deque()

    def __repr__(self) -> str:
        return "DijkstraSearch:\n" + super().__repr__()

    @validate_labels('start_label')
    def run(self, start_label: str):
        """Performs Dijkstra search starting from the given vertex label."""
        start_vertex = self._get_vertex(start_label)

        if start_vertex is None:
            raise ValueError(f"Vertex with label '{start_label}' does not exist.")

        self._reset('dijkstra')

        start_vertex.update_dijkstra_attributes(distance=0)

        for vertex in self._get_vertices():
            self.__queue.append(vertex)

        while self.__queue:
            current_vertex = self.__min_vertex()

            for edge in current_vertex.get_edges():
                source = edge.get_source()
                destination = edge.get_destination()
                weight = edge.get_weight()

                if destination.get_distance() >= source.get_distance() + weight:
                    destination.update_default_attributes(predecessor=source)
                    destination.update_dijkstra_attributes(distance=source.get_distance() + weight)

            self.__single_source.append(current_vertex)

    def __min_vertex(self) -> Vertex:
        """Gets the vertex whose distance is the least in the queue"""
        min_distance: int | float = float('inf')
        min_vertex: Vertex = Vertex('None')

        for vertex in self.__queue:
            if vertex.get_distance() < min_distance:
                min_distance = vertex.get_distance()
                min_vertex = vertex

        self.__queue.remove(min_vertex)

        return min_vertex
