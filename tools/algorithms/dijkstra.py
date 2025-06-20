"""Module that implements Dijkstra's algorithm using existing Graph structure."""

from collections import deque

from matplotlib import pyplot as plt

import networkx as nx
from networkx import MultiDiGraph

from tools.api.graph import Graph
from tools.api.object import Vertex

class DijkstraSearch(Graph):
    """A class to perform Dijkstra search on a graph"""

    def __init__(self):
        super().__init__()
        self.__queue: deque['Vertex'] = deque()
        self.__is_run: bool = False

    def __add_to_graph(
            self,
            graph: MultiDiGraph,
            vertex: Vertex,
            labels: dict[Vertex, str],
            colors: dict[Vertex, str],
            edge_labels: dict[tuple[Vertex, Vertex], str]
        ):
        """Performs processes of adding a node and an edge to graph visualization."""
        graph.add_node(vertex)

        for edge in vertex.get_edges():
            if self.__is_run:
                if edge.get_destination().get_predecessor() is vertex:
                    graph.add_edge(vertex, edge.get_destination())
                    edge_labels[(vertex, edge.get_destination())] = str(edge.get_weight())
            else:
                graph.add_edge(vertex, edge.get_destination())
                edge_labels[(vertex, edge.get_destination())] = str(edge.get_weight())

        labels[vertex] = str(vertex.get_label()) + "\n" + str(vertex.get_distance())
        colors[vertex] = vertex.get_color()

        return graph, labels, colors

    def visualize(self):
        """Visualizes the graph."""
        graph: MultiDiGraph = MultiDiGraph()
        labels: dict[Vertex, str] = {}
        colors: dict[Vertex, str] = {}
        edge_labels: dict[tuple[Vertex, Vertex], str] = {}

        for vertex in self.get_vertices():
            self.__add_to_graph(graph, vertex, labels, colors, edge_labels)

        if self.__is_run:
            pos = nx.spiral_layout(graph)
        else:
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

        if self.__is_run:
            nx.draw_networkx_edge_labels(
                graph, pos,
                edge_labels=edge_labels
            )

        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def run(self, start: Vertex):
        """Performs Dijkstra search starting from the given vertex label."""
        self._reset('dijkstra')

        start.update_dijkstra_attributes(distance=0)

        for vertex in self._get_vertices():
            self.__queue.append(vertex)

        while self.__queue:
            current_vertex = self.__min_vertex()

            for edge in current_vertex.get_edges():
                source = edge.get_source()
                destination = edge.get_destination()
                weight = edge.get_weight()

                if destination.get_distance() >= source.get_distance() + weight:
                    destination.update_dijkstra_attributes(
                        predecessor=source,
                        distance=source.get_distance() + weight
                    )

        self.__is_run = True

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

    def get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self._get_vertices()
