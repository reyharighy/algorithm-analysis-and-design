"""Module that implements Kruskal's algorithm using existing Graph structure."""

from matplotlib import pyplot as plt

import networkx as nx
from networkx import Graph as G

from tools.api.graph import Graph
from tools.api.object import Vertex, Edge

class KruskalSearch(Graph):
    """A class to perform Kruskal search on a graph"""

    def __init__(self):
        super().__init__()
        self.__trees: list[set[Edge]] = []
        self.__is_run: bool = False

    def visualize(self):
        """Visualizes the graph."""
        graph: G = G().to_undirected()
        labels: dict[Vertex, str] = {}
        all_edges: list[Edge] = []
        edge_labels: dict[tuple[Vertex, Vertex], str] = {}

        if self.__is_run:
            for edge in self.__trees[0]:
                graph.add_node(edge.get_source())
                graph.add_node(edge.get_destination())
                labels[edge.get_source()] = str(edge.get_source().get_label())
                labels[edge.get_destination()] = str(edge.get_destination().get_label())
                graph.add_edge(edge.get_source(), edge.get_destination(), weight=edge.get_weight())
                edge_labels[(edge.get_source(), edge.get_destination())] = str(edge.get_weight())
        else:
            for vertex in self.get_vertices():
                graph.add_node(vertex)
                labels[vertex] = str(vertex.get_label())
                all_edges.extend(vertex.get_edges())

            for edge in all_edges:
                graph.add_edge(edge.get_source(), edge.get_destination())
                edge_labels[(edge.get_source(), edge.get_destination())] = str(edge.get_weight())

        pos = nx.kamada_kawai_layout(graph)

        plt.figure(figsize=(20, 20))

        nx.draw_networkx_nodes(
            graph, pos,
            node_color='gray',
            node_size=1000,
            edgecolors='black'
        )

        nx.draw_networkx_edges(
            graph, pos,
            width=2,
            edge_color='gray',
            arrows=True,
            arrowsize=20,
            arrowstyle='<|-|>',
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

    def __get_tree(self, vertex: Vertex) -> set[Edge] | None:
        """Gets a tree in which a vertex is included."""
        for tree in self.__trees:
            for edge in tree:
                if vertex in [edge.get_source(), edge.get_destination()]:
                    return tree

        return None

    def run(self):
        """Performs Kruskal search on graph."""
        vertices: list[Vertex] = self.get_vertices()
        all_edges: list[Edge] = []

        for vertex in vertices:
            all_edges.extend(vertex.get_edges())

        all_edges.sort(key=lambda edge: edge.get_weight())

        for edge in all_edges:
            source = edge.get_source()
            destination = edge.get_destination()

            source_tree = self.__get_tree(source)
            destination_tree = self.__get_tree(destination)

            if source_tree is None and destination_tree is None:
                self.__trees.append(set([edge]))

            elif source_tree and destination_tree is None:
                self.__trees.append(source_tree.union([edge]))
                self.__trees.remove(source_tree)

            elif source_tree is None and destination_tree:
                self.__trees.append(destination_tree.union([edge]))
                self.__trees.remove(destination_tree)

            elif source_tree and destination_tree:
                if source_tree == destination_tree:
                    continue

                self.__trees.append(source_tree.union([edge]).union(destination_tree))
                self.__trees.remove(source_tree)
                self.__trees.remove(destination_tree)

        self.__is_run = True

    def get_vertices(self) -> list[Vertex]:
        """Returns the list of vertices in the graph."""
        return self._get_vertices()

    def get_trees(self) -> list[set[Edge]]:
        """Returns the established MST in the graph."""
        return self.__trees
