"""This module defines a Graph class that represents a graph using vertices and edges."""

from object import Vertex, Edge
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
    def add_vertex(self, label: str):
        """Adds a vertex with the given label to the graph."""
        if self._get_vertex(label) is None:
            vertex = Vertex(label)
            self.__vertices.append(vertex)

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

    def _reset(self, include: str):
        """Resets the graph's vertices to their initial state."""
        for vertex in self.__vertices:
            vertex.update_default_attributes(
                predecessor=None,
                color='white'
            )

            match include:
                case 'bfs':
                    vertex.update_bfs_attributes(distance=float('inf'))
                case 'dfs':
                    vertex.update_dfs_attributes(
                        discovery_time=0,
                        finish_time=0
                    )
                case _:
                    raise ValueError(f'{include} is incorrect value for parameter include')

    def create_graph_from_problem_statement(self, task_number: int):
        """Creates a graph from a problem statement."""

        match task_number:
            case 1:
                self.__create_graph_task_1()
            case 2:
                self.__create_graph_task_2()
            case 3:
                self.__create_graph_task_3()
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
                
    def __create_graph_task_2(self):
        """Creates a graph for task 2 with weighted edges for Prim's and Kruskal's algorithms."""
        for label in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
            self.add_vertex(label)

        edges = [
            ('A', 'C', 4), ('A', 'E', 14),
            ('C', 'D', 4), ('C', 'K', 20),
            ('D', 'E', 7), ('D', 'F', 9),
            ('F', 'G', 8), ('F', 'K', 11), 
            ('E', 'G', 12),
            ('G', 'H', 11),
            ('H', 'K', 15), ('H', 'J', 7), ('H', 'I', 4),
            ('K', 'J', 7),
            ('I', 'B', 3), ('I', 'J', 5),
            ('B', 'J', 7)
        ]

        for src, dest, weight in edges:
            self.add_edge(src, dest, (weight, weight))
    
    def __create_graph_task_3(self):
        """Creates a graph for task 3 with weighted edges for Dijkstra."""
        for label in ['S', 'U', 'X', 'V', 'Y']:
            self.add_vertex(label)

        self.add_edge('S', 'U', 10)
        self.add_edge('S', 'X', 5)
        self.add_edge('Y', 'S', 7)
        self.add_edge('U', 'V', 1)
        self.add_edge('U', 'X', 2)
        self.add_edge('X', 'U', 3)
        self.add_edge('X', 'V', 9)
        self.add_edge('X', 'Y', 2)
        self.add_edge('Y', 'V', 6)
        self.add_edge('V', 'Y', 4)

    def _get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self.__vertices

    def _get_edges(self) -> list['Edge']:
        """Returns the list of edge in the graph"""
        edges: list[Edge] = []

        for vertex in self.__vertices:
            edges.extend(vertex.get_edges())

        return edges
