"""This module defines a Graph class that represents a graph using vertices and edges."""

from object import Vertex, Edge
from helper.validators import validate_labels

class Graph:
    """A class representing a graph, which consists of vertices and edges."""

    def __init__(self):
        self.__vertices: list[Vertex] = []

    def __repr__(self) -> str:
        """Returns a string representation of the graph."""
        if not self.__vertices:
            return 'Graph is empty.'

        s = ''

        for vertex in self.__vertices:
            s += f'- Vertex({vertex.get_label()}): {vertex.get_edges()}'

            if vertex.get_label() != self.__vertices[-1].get_label():
                s += '\n'

        return s

    @validate_labels('label')
    def _get_vertex(self, label: str) -> 'Vertex | None':
        """Retrieves a vertex by its label."""
        for vertex in self.__vertices:
            if vertex.get_label() == label:
                return vertex

        return None

    @validate_labels('src', 'dest')
    def __get_src_dest(self, src: str, dest: str) -> tuple[Vertex | None, Vertex | None]:
        """Checks if both source and destination vertices exist."""
        source_vertex = self._get_vertex(src)
        dest_vertex = self._get_vertex(dest)

        return (source_vertex, dest_vertex)

    @validate_labels('label')
    def __add_vertex(self, label: str):
        """Adds a vertex with the given label to the graph."""
        if self._get_vertex(label) is None:
            vertex = Vertex(label)
            self.__vertices.append(vertex)

    @validate_labels('source_label', 'dest_label')
    def __add_edge(self, source_label: str, dest_label: str, weight: int | tuple[int, int] = 1):
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

    def _reset(self, include: str):
        """Resets the graph's vertices to their initial state."""
        for vertex in self.__vertices:
            vertex.update_default_attributes(color='white', predecessor=None)

            match include:
                case 'bfs':
                    vertex.update_bfs_attributes(distance=float('inf'))
                case 'dfs':
                    vertex.update_dfs_attributes(discovery_time=0, finish_time=0)
                case 'dijkstra':
                    vertex.update_dijkstra_attributes(distance=float('inf'))
                case _:
                    raise ValueError(f'{include} is incorrect value for parameter include')

    def create_graph_from_problem_statement(self, task_number: int):
        """Creates a graph from a problem statement."""

        match task_number:
            case 1:
                self.__create_graph_task_1()
            case 3:
                self.__create_graph_task_3()
            case _:
                raise ValueError("Invalid task number")

    def __create_graph_task_1(self):
        """Creates a graph for task 1."""
        for i in range(65, 75):
            self.__add_vertex(chr(i))

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
                self.__add_edge(source, d)

    def __create_graph_task_3(self):
        """Creates a graph for task 3 with weighted edges for Dijkstra."""
        for label in ['S', 'U', 'X', 'V', 'Y']:
            self.__add_vertex(label)

        edge_dictionary = {
            'S': [('U', 10), ('X', 5)],
            'U': [('V', 1), ('X', 2)],
            'V': [('Y', 4)],
            'X': [('U', 3), ('V', 9), ('Y', 2)],
            'Y': [('S', 7), ('V', 6)]
        }

        for source, dest in edge_dictionary.items():
            for d, w in dest:
                self.__add_edge(source, d, w)

    def _get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self.__vertices
