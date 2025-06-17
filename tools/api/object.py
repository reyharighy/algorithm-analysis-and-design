"""This module defines objects used in graph representation, including Vertex and Edge classes."""

from typing import Unpack
from dataclasses import dataclass
from helper.validators import validate_labels, validate_param_keyword
from helper.vertex_types import BFSVertexType, DFSVertexType, DijkstraVertexType
from helper.edge_types import DFSEdgeType

@dataclass
class SpecialVertexAttributes:
    """A dataclass that specifies attributes when working with the vertex."""
    color: str = "white"
    predecessor: 'Vertex | None' = None
    distance: int | float = float('inf')
    discovery_time: int = 0
    finish_time: int = 0

class Vertex:
    """A class representing a vertex in a graph."""

    @validate_labels('label')
    def __init__(self, label: str):
        self.__label: str = label
        self.__special_attributes: SpecialVertexAttributes = SpecialVertexAttributes()
        self.__edges: list[Edge] = []

    def __repr__(self) -> str:
        """Returns a string representation of the edge."""
        return f"Vertex({self.get_label()})"

    def definition(self, algorithm: str) -> str:
        """Returns the definition of the vertex."""
        vertex = ''

        vertex += f"Vertex({{label: {self.get_label()}"

        match algorithm:
            case 'bfs':
                vertex += f", color: {self.get_color()}"
                vertex += f", predecessor: {self.get_predecessor()}"
                vertex += f", distance: {self.get_distance()}"
            case 'dfs':
                vertex += f", color: {self.get_color()}"
                vertex += f", predecessor: {self.get_predecessor()}"
                vertex += f", discovery: {self.get_discovery_time()}"
                vertex += f", finish: {self.get_finish_time()}"
            case 'dijkstra':
                vertex += f", predecessor: {self.get_predecessor()}"
                vertex += f", distance: {self.get_distance()}"

        edge_list = '['

        for i, edge in enumerate(self.get_edges()):
            if i != 0:
                edge_list += ', '

            edge_list += edge.definition(algorithm)

        edge_list += ']'

        vertex += f", edges: {edge_list}}})"

        return vertex

    # -------------------------------------------------------------------------------
    # List of getter functions to all attributes of a vertex
    # -------------------------------------------------------------------------------

    def get_label(self) -> str | None:
        """Returns the label of the vertex."""
        return self.__label

    def get_color(self) -> str:
        """Returns the color of the vertex."""
        return self.__special_attributes.color

    def get_predecessor(self) -> 'Vertex | None':
        """Returns the predecessor of the vertex."""
        return self.__special_attributes.predecessor

    def get_edges(self) -> list['Edge']:
        """Returns a list of edges that connect to other vertices."""
        return self.__edges

    def get_distance(self) -> int | float:
        """Returns the BFS distance of the vertex."""
        return self.__special_attributes.distance

    def get_discovery_time(self) -> int | float:
        """Returns the DFS discovery time of the vertex."""
        return self.__special_attributes.discovery_time

    def get_finish_time(self) -> int | float:
        """Returns the DFS finish time of the vertex."""
        return self.__special_attributes.finish_time

    # -------------------------------------------------------------------------------
    # END
    # -------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------
    # List of setter functions to all attributes of a vertex, except edge.
    # Edge should only be modified directly in the Edge class.
    # -------------------------------------------------------------------------------

    def __update(self, this, **kwargs):
        """Update after successfull validation of parameter keyword input."""
        for key, value in kwargs.items():
            if hasattr(this, key):
                setattr(this, key, value)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")

    @validate_param_keyword(BFSVertexType.__annotations__.keys())
    def update_bfs_attributes(self, **kwargs: Unpack[BFSVertexType]):
        """
        Updates BFS-specific attributes of the vertex, including:
        - Color
        - Predecessor
        - Distance
        """
        self.__update(self.__special_attributes, **kwargs)

    @validate_param_keyword(DFSVertexType.__annotations__.keys())
    def update_dfs_attributes(self, **kwargs: Unpack[DFSVertexType]):
        """
        Updates DFS-specific attributes of the vertex.
        - Color
        - Predecessor
        - Discovery Time
        - Finish Time
        """
        self.__update(self.__special_attributes, **kwargs)

    @validate_param_keyword(DijkstraVertexType.__annotations__.keys())
    def update_dijkstra_attributes(self, **kwargs: Unpack[DijkstraVertexType]):
        """
        Updates Dijkstra-specific attributes of the vertex.
        - Predecessor
        - Distance
        """
        self.__update(self.__special_attributes, **kwargs)

    # -------------------------------------------------------------------------------
    # END
    # -------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------
    # List of additional functions related to vertex when operating with graph.
    # -------------------------------------------------------------------------------

    def add_edge(self, edge: 'Edge'):
        """Adds an edge to the vertex."""
        self.__edges.append(edge)

    # -------------------------------------------------------------------------------
    # END
    # -------------------------------------------------------------------------------

@dataclass
class SpecialEdgeAttributes:
    """A dataclass that specifies attributes when working with the edge."""
    weight: int
    classification: str | None = None

class Edge:
    """A class representing an edge in a graph."""

    def __init__(self, source: Vertex, destination: Vertex, weight: int = 1):
        self.__source = source
        self.__destination = destination
        self.__special_attributes: SpecialEdgeAttributes = SpecialEdgeAttributes(weight)

    def __repr__(self) -> str:
        """Returns a string representation of the edge."""
        s = f"Edge({self.__source.get_label()}"
        s += f", {self.__destination.get_label()}"
        s += f", {self.get_weight()})"

        return s

    def definition(self, algorithm: str) -> str:
        """Returns the definition of the edge."""
        s = f"Edge({self.__source.get_label()}"
        s += f", {self.__destination.get_label()}"

        match algorithm:
            case 'dfs':
                s += f", {self.get_classification()}"
            case "kruskal":
                s += f", {self.get_weight()}"
            case "prim":
                s += f", {self.get_weight()}"
            case 'dijkstra':
                s += f", {self.get_weight()}"

        s += ')'

        return s

    # -------------------------------------------------------------------------------
    # List of getter functions to all attributes of an edge
    # -------------------------------------------------------------------------------

    def get_source(self) -> Vertex:
        """Returns the source vertex of an edge."""
        return self.__source

    def get_destination(self) -> Vertex:
        """Returns the destination vertex of an edge."""
        return self.__destination

    def get_weight(self) -> int:
        """Returns the weight of a vertex."""
        return self.__special_attributes.weight

    def get_classification(self) -> str | None:
        """Returns the classification of an edge when running DFS."""
        return self.__special_attributes.classification

    # -------------------------------------------------------------------------------
    # END
    # -------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------
    # List of setter functions to all attributes of an edge, except the source and
    # the destination vertices. They should only be modified directly in the vertex
    # class.
    # -------------------------------------------------------------------------------

    def __update(self, this, **kwargs):
        """Update after successfull validation of parameter keyword input."""
        for key, value in kwargs.items():
            if hasattr(this, key):
                setattr(this, key, value)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")

    @validate_param_keyword(DFSEdgeType.__annotations__.keys())
    def update_dfs_attributes(self, **kwargs: Unpack[DFSEdgeType]):
        """
        Updates DFS-specific attributes of the edge, including:
        - Classification
        """
        self.__update(self.__special_attributes, **kwargs)

    # -------------------------------------------------------------------------------
    # END
    # -------------------------------------------------------------------------------
