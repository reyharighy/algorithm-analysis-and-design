"""A module to perform depth-first search on a graph."""

from matplotlib import pyplot as plt

import networkx as nx
from networkx import DiGraph

from tools.api.graph import Graph
from tools.api.object import Vertex

class DepthFirstSearch(Graph):
    """A class to perform depth-first search on a graph."""

    def __init__(self):
        super().__init__()
        self.__time = 0
        self.__is_run: bool = False
        self.__start: Vertex | None = None

    def __add_to_graph(
            self,
            graph: DiGraph,
            vertex: Vertex,
            labels: dict[Vertex, str],
            colors: dict[Vertex, str],
            edge_labels: dict[tuple[Vertex, Vertex], str]
        ):
        """Performs processes of adding a node and an edge to graph visualization."""
        graph.add_node(vertex, distance=vertex.get_distance())

        for edge in vertex.get_edges():
            graph.add_edge(vertex, edge.get_destination(), classification=edge.get_classification())
            edge_labels[(vertex, edge.get_destination())] = str(edge.get_classification())

        dis_fin_time = str(vertex.get_discovery_time()) + '/' + str(vertex.get_finish_time())
        labels[vertex] = str(vertex.get_label()) + "\n" + dis_fin_time
        colors[vertex] = vertex.get_color()

        return graph, labels, colors

    def visualize(self):
        """Visualizes the graph."""
        graph: DiGraph = DiGraph()
        labels: dict[Vertex, str] = {}
        colors: dict[Vertex, str] = {}
        edge_labels: dict[tuple[Vertex, Vertex], str] = {}

        for vertex in self.get_vertices():
            if self.__is_run:
                if vertex.get_predecessor() or vertex is self.__start:
                    self.__add_to_graph(graph, vertex, labels, colors, edge_labels)
            else:
                self.__add_to_graph(graph, vertex, labels, colors, edge_labels)

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

        nx.draw_networkx_edge_labels(
            graph, pos,
            edge_labels=edge_labels
        )

        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def run(self, start: Vertex):
        """Performs depth-first search starting from the given vertex label."""
        self._reset('dfs')
        self.__dfs_visit(start)
        self.__start = start
        self.__is_run = True

    def __dfs_visit(self, vertex: Vertex):
        """Visits a vertex and explores its neighbors recursively."""
        self.__time += 1

        vertex.update_dfs_attributes(color="red", discovery_time=self.__time)

        if len(vertex.get_edges()) < 1:
            self.__update_isolated_vertices(vertex)
            return

        for edge in vertex.get_edges():
            if edge.get_destination().get_color() == 'gray':
                edge.update_dfs_attributes(classification='T')
                edge.get_destination().update_dfs_attributes(predecessor=vertex)
                self.__dfs_visit(edge.get_destination())

            elif edge.get_destination().get_color() == 'red':
                edge.update_dfs_attributes(classification='B')

            elif edge.get_destination().get_color() == 'lightblue':
                source_time = vertex.get_discovery_time()
                destination_time = edge.get_destination().get_discovery_time()

                if source_time < destination_time:
                    edge.update_dfs_attributes(classification='F')
                else:
                    edge.update_dfs_attributes(classification='C')

        self.__update_isolated_vertices(vertex)

    def __update_isolated_vertices(self, vertex: Vertex):
        """Updates the attributes of isolated vertices."""
        self.__time += 1
        vertex.update_dfs_attributes(color='lightblue', finish_time=self.__time)

    def get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self._get_vertices()
