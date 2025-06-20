"""This module defines a Graph class that represents a graph using vertices and edges."""

from tools.api.object import Vertex, Edge
from helper.validators import validate_labels

class Graph:
    """A class representing a graph, which consists of vertices and edges."""

    def __init__(self):
        self.__vertices: list[Vertex] = []

    def definition(self, algorithm: str) -> str:
        """Returns the definition of the graph."""
        vertices = '\n\tGraph Definition:\n'

        if not self.__vertices:
            vertices += '\t  Graph is empty'

        for vertex in self.__vertices:
            vertices += "\t  - "

            match algorithm:
                case 'bfs':
                    vertices += vertex.definition('bfs')
                case 'dfs':
                    vertices += vertex.definition('dfs')
                case 'kruskal':
                    vertices += vertex.definition('kruskal')
                case 'prim':
                    vertices += vertex.definition('prim')
                case 'dijkstra':
                    vertices += vertex.definition('dijkstra')

            if vertex.get_label() != self.__vertices[-1].get_label():
                vertices += '\n'

        return vertices + '\n'

    def _get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self.__vertices

    @validate_labels('label')
    def get_vertex(self, label: str) -> 'Vertex | None':
        """Retrieves a vertex by its label."""
        for vertex in self.__vertices:
            if vertex.get_label() == label:
                return vertex

        return None

    @validate_labels('label')
    def add_vertex(self, label: str) -> bool:
        """Adds a vertex with the given label to the graph."""
        if self.get_vertex(label) is None:
            vertex = Vertex(label)
            self.__vertices.append(vertex)
            return True

        return False

    def add_edge(self, source: Vertex, destination: Vertex, weight: int | tuple[int, int] = 1):
        """Adds an edge between two vertices in the graph."""
        from_src: Edge | None = None

        if isinstance(weight, int) and weight > 0:
            from_src = Edge(source, destination, weight)

        if isinstance(weight, tuple) and len(weight) == 2 and weight[0] > 0 and weight[1] > 0:
            from_src = Edge(source, destination, weight[0])
            from_dest = Edge(destination, source, weight[-1])
            destination.add_edge(from_dest)

        if isinstance(from_src, Edge):
            source.add_edge(from_src)

    def _reset(self, algorithm: str):
        """Resets the graph's vertices to their initial state."""
        for vertex in self.__vertices:
            match algorithm:
                case 'bfs':
                    vertex.update_bfs_attributes(
                        color="gray",
                        predecessor=None,
                        distance=float('inf')
                    )
                case 'dfs':
                    vertex.update_dfs_attributes(
                        color="gray",
                        predecessor=None,
                        discovery_time=0,
                        finish_time=0
                    )
                case 'dijkstra':
                    vertex.update_dijkstra_attributes(
                        predecessor=None,
                        distance=float('inf')
                    )
                case _:
                    raise ValueError(f'{algorithm} is incorrect value for parameter include')

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
            'I': ['H', 'G'],
            'J': [],
        }

        for source_label, destination_labels in edge_dictionary.items():
            source = self.get_vertex(source_label)

            for label in destination_labels:
                destination = self.get_vertex(label)

                if source and destination:
                    self.add_edge(source, destination)

    def __create_graph_task_2(self):
        """Creates a graph for task 2 with weighted edges."""
        for i in range(65, 76):
            self.add_vertex(chr(i))

        edge_dictionary = {
            'A': [('C', 4), ('B', 14)],
            'B': [('D', 7), ('E', 12)],
            'C': [('D', 4), ('G', 20)],
            'D': [('F', 9)],
            'E': [('F', 8), ('H', 11)],
            'F': [('G', 11)],
            'G': [('H', 15), ('I', 7)],
            'H': [('I', 7), ('J', 4)],
            'I': [('J', 5), ('K', 7)],
            'J': [('K', 3)]
        }

        for source_label, destination_labels in edge_dictionary.items():
            source = self.get_vertex(source_label)

            for label, weight in destination_labels:
                destination = self.get_vertex(label)

                if source and destination:
                    self.add_edge(source, destination, (weight, weight))

    def __create_graph_task_3(self):
        """Creates a graph for task 3 with weighted edges for Dijkstra."""
        for label in ['S', 'U', 'X', 'V', 'Y']:
            self.add_vertex(label)

        edge_dictionary = {
            'S': [('U', 10), ('X', 5)],
            'U': [('V', 1), ('X', 2)],
            'V': [('Y', 4)],
            'X': [('U', 3), ('V', 9), ('Y', 2)],
            'Y': [('S', 7), ('V', 6)]
        }

        for source_label, destination_labels in edge_dictionary.items():
            source = self.get_vertex(source_label)

            for label, weight in destination_labels:
                destination = self.get_vertex(label)

                if source and destination:
                    self.add_edge(source, destination, weight)
