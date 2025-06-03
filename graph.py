"""This module defines a Graph class that represents a graph using vertices and edges."""

from typing import Unpack
from object import Vertex, Edge, VertexDefaultAttributes
from validators import validate_labels

class Graph:
    """A class representing a graph, which consists of vertices and edges."""

    def __init__(self):
        self.__vertices: list[Vertex] = []

    def __repr__(self) -> str:
        """Returns a string representation of the graph."""
        if not self.__vertices:
            # If there are no vertices, return a message indicating that.
            return 'Graph is empty.'

        s = ''

        for vertex in self.__vertices:
            s += f'- Vertex({vertex.get_label()}): {vertex.get_edges()}'

            if vertex.get_label() != self.__vertices[-1].get_label():
                s += '\n'

        return s

    def _get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self.__vertices

    def _get_vertex(self, label: str) -> 'Vertex | None':
        """Retrieves a vertex by its label."""
        for vertex in self.__vertices:
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
            self.__vertices.append(vertex)

    @validate_labels('vertex_label')
    def update_vertex(self, vertex_label: str, **kwargs: Unpack[VertexDefaultAttributes]):
        """Updates the properties of a vertex."""
        vertex = self._get_vertex(vertex_label)

        if vertex is None:
            raise ValueError(f"Vertex with label '{vertex_label}' does not exist.")

        vertex.update_default_attributes(**kwargs)

    @validate_labels('source_label', 'dest_label')
    def add_edge(self, source_label: str, dest_label: str, weight: int | tuple[int, int] = 1):
        """Adds an edge between two vertices in the graph."""
        source_vertex, dest_vertex = self.__get_src_dest(source_label, dest_label)

        if not source_vertex or not dest_vertex:
            raise ValueError(f"'{source_label}' or '{dest_label}' do not exist.")

        from_src: Edge | None = None

        if isinstance(weight, int) and weight > 0:
            from_src = Edge(source_vertex, dest_vertex, weight)
        elif isinstance(weight, tuple) and len(weight) == 2 and weight[0] > 0 and weight[1] > 0:
            from_src = Edge(source_vertex, dest_vertex, weight[0])
            from_dest = Edge(dest_vertex, source_vertex, weight[1])
            dest_vertex.add_edge(from_dest)
        else:
            raise ValueError("It should be a positive integer or a tuple of two positive integers.")

        source_vertex.add_edge(from_src)

    @validate_labels('source_label', 'dest_label')
    def update_edge(self, source_label: str, dest_label: str, new_weight: int):
        """Updates the properties of an edge between two vertices."""
        source_vertex, dest_vertex = self.__get_src_dest(source_label, dest_label)

        if source_vertex is None or dest_vertex is None:
            raise ValueError(f"'{source_label}' or '{dest_label}' do not exist.")

        for edge in source_vertex.get_edges():
            if edge.destination == dest_vertex:
                edge.update_weight(new_weight)
                return

    def _reset(self, include: str):
        """Resets the graph's vertices to their initial state."""
        for vertex in self.__vertices:
            vertex.update_default_attributes(
                predecessor=None,
                color='white'
            )

            match include:
                case 'bfs':
                    vertex.update_bfs_attributes(
                        distance=float('inf')
                    )

    def create_graph_from_problem_statement(self, task_number: int):
        """Creates a graph from a problem statement."""

        match task_number:
            case 1:
                self.__create_graph_task_1()
            case _:
                raise ValueError("Invalid task number")

    def __create_graph_task_1(self):
        """Creates a graph for task 1."""
        for i in range(65, 75):
            self.add_vertex(chr(i))

        edge_dictionary = {
            'A': ['B', 'D', 'E'],
            'B': ['C', 'D'],
            'C': ['G', 'H'],
            'D': ['F'],
            'E': ['D', 'F'],
            'F': ['J'],
            'G': [],
            'H': ['G'],
            'I': ['G', 'H'],
            'J': [],
        }

        for source, dest in edge_dictionary.items():
            for d in dest:
                self.add_edge(source, d)
