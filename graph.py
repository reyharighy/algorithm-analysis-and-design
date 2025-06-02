"""This module defines a Graph class that represents a graph using vertices and edges."""

from typing import Unpack
from object import Vertex, Edge, VertexAttributes
from validators import validate_labels

class Graph:
    """A class representing a graph, which consists of vertices and edges."""

    def __init__(self):
        self._vertices: list[Vertex] = []

    def __repr__(self) -> str:
        """Returns a string representation of the graph."""
        if not self._vertices:
            return 'Graph is empty.'

        s = ''

        for vertex in self._vertices:
            s += f'- Vertex({vertex.get_label()}): {vertex.get_edges()}'

            if vertex.get_label() != self._vertices[-1].get_label():
                s += '\n'

        return s

    def _get_vertex(self, label: str) -> 'Vertex | None':
        """Retrieves a vertex by its label."""
        for vertex in self._vertices:
            if vertex.get_label() == label:
                return vertex

        return None

    def __get_src_dest(self, src: str, dest: str) -> tuple[Vertex | None, Vertex | None]:
        """Checks if both source and destination vertices exist."""
        source_vertex = self._get_vertex(src)
        dest_vertex = self._get_vertex(dest)

        return (source_vertex, dest_vertex)

    @validate_labels('label')
    def add_vertex(self, label: str):
        """Adds a vertex with the given label to the graph."""
        if self._get_vertex(label) is None:
            vertex = Vertex(label)
            self._vertices.append(vertex)

    @validate_labels('vertex_label')
    def update_vertex(self, vertex_label: str, **kwargs: Unpack[VertexAttributes]):
        """Updates the properties of a vertex."""
        vertex = self._get_vertex(vertex_label)

        if vertex is None:
            return

        vertex.update_attributes(**kwargs)

    @validate_labels('source_label', 'dest_label')
    def add_edge(self, source_label: str, dest_label: str, weight: int | tuple[int, int] = 1):
        """Adds an edge between two vertices in the graph."""
        source_vertex, dest_vertex = self.__get_src_dest(source_label, dest_label)

        if not source_vertex or not dest_vertex:
            return

        from_src: Edge | None = None

        if isinstance(weight, int) and weight > 0:
            from_src = Edge(source_vertex, dest_vertex, weight)
        elif isinstance(weight, tuple) and len(weight) == 2 and weight[0] > 0 and weight[1] > 0:
            from_src = Edge(source_vertex, dest_vertex, weight[0])
            from_dest = Edge(dest_vertex, source_vertex, weight[1])
            dest_vertex.add_edge(from_dest)
        else:
            return

        source_vertex.add_edge(from_src)

    @validate_labels('source_label', 'dest_label')
    def update_edge(self, source_label: str, dest_label: str, new_weight: int):
        """Updates the properties of an edge between two vertices."""
        source_vertex, dest_vertex = self.__get_src_dest(source_label, dest_label)

        if source_vertex is None or dest_vertex is None:
            return

        for edge in source_vertex.get_edges():
            if edge.destination == dest_vertex:
                edge.update_weight(new_weight)
                return
