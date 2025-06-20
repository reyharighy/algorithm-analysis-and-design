"""A module to perform breadth-first search on a graph."""

from collections import deque
from matplotlib import pyplot as plt

import networkx as nx
from networkx import DiGraph

from tools.api.graph import Graph
from tools.api.object import Vertex

class BreadthFirstSearch(Graph):
    """A class to perform breadth-first search on a graph."""

    def __init__(self):
        super().__init__()
        self.__queue: deque['Vertex'] = deque()
        self.__is_run: bool = False
        self.__start: Vertex | None = None

    def __add_to_graph(
            self,
            graph: DiGraph,
            vertex: Vertex,
            labels: dict[Vertex, str],
            colors: dict[Vertex, str]
        ):
        """Performs processes of adding a node and an edge to graph visualization."""
        graph.add_node(vertex, distance=vertex.get_distance())

        for edge in vertex.get_edges():
            graph.add_edge(vertex, edge.get_destination())

        labels[vertex] = str(vertex.get_label()) + ":" + str(vertex.get_distance())
        colors[vertex] = vertex.get_color()

        return graph, labels, colors

    def visualize(self):
        """Visualizes the graph."""
        graph: DiGraph = DiGraph()
        labels: dict[Vertex, str] = {}
        colors: dict[Vertex, str] = {}

        for vertex in self.get_vertices():
            if self.__is_run:
                if vertex.get_predecessor() or vertex is self.__start:
                    self.__add_to_graph(graph, vertex, labels,colors)
            else:
                self.__add_to_graph(graph, vertex, labels,colors)

        pos = nx.kamada_kawai_layout(graph)

        nx.draw_networkx_nodes(
            graph, pos,
            node_color=list(colors.values()), # type: ignore
            node_size=1000,
            edgecolors='black'
        )

        nx.draw_networkx_edges(
            graph, pos,
            width=2,
            edge_color='gray',
            arrows=True,
            arrowsize=20,
            arrowstyle='-|>',
        )

        nx.draw_networkx_labels(
            graph, pos,
            labels=labels,
            font_size=10,
            font_family='sans-serif'
        )

        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def run(self, start: Vertex):
        """Performs breadth-first search starting from the given vertex label."""
        self._reset('bfs')

        start.update_bfs_attributes(color="red", distance=0)

        self.__queue.append(start)
        self.__start = start

        while self.__queue:
            head = self.__queue.popleft()

            for edge in head.get_edges():
                destination = edge.get_destination()

                if destination.get_color() == 'gray':
                    destination.update_bfs_attributes(
                        color='red',
                        predecessor=head,
                        distance=head.get_distance() + 1
                    )

                    self.__queue.append(destination)

            head.update_bfs_attributes(color='lightblue')

        self.__is_run = True

    def get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self._get_vertices()
