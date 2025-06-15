"""This module defines objects used in graph representation, including Vertex and Edge classes."""

from typing import Unpack
from dataclasses import dataclass
from helper.validators import validate_labels, validate_param_keyword
from helper.vertex_types import DefaultVertexType, BFSVertexType, DFSVertexType, DijkstraVertexType
from helper.edge_types import DefaultEdgeType, DFSEdgeType

@dataclass
class DefaultVertexAttributes:
    """A dataclass that's related to default attributes in a vertex."""
    label: str | None = None
    color: str = "white"
    predecessor: 'Vertex | None' = None

@dataclass
class SpecialVertexAttributes:
    """A dataclass that specifies attributes when working with the vertex."""
    distance: int | float = float('inf')
    discovery_time: int = 0
    finish_time: int = 0

class Vertex:
    """A class representing a vertex in a graph."""

    @validate_labels('label')
    def __init__(self, label: str):
        self.__default_attributes: DefaultVertexAttributes = DefaultVertexAttributes(label)
        self.__special_attributes: SpecialVertexAttributes = SpecialVertexAttributes()
        self.__edges: list[Edge] = []

    def definition(self, algorithm: str) -> str:
        """Returns a string representation of the vertex."""
        vertex = ''

        vertex += f"Vertex({{label: {self.get_label()}"
        vertex += f", color: {self.get_color()}"
        vertex += f", predecessor: {self.get_predecessor()}"
        vertex += f", edges: {self.get_edges()}"

        match algorithm:
            case 'bfs':
                vertex += f", distance: {self.get_distance()}"

        vertex += "})"

        return vertex

    # -------------------------------------------------------------------------------
    # List of getter functions to all attributes of a vertex
    # -------------------------------------------------------------------------------

    def get_label(self) -> str | None:
        """Returns the label of the vertex."""
        if self.__default_attributes.label:
            return self.__default_attributes.label

        return None

    def get_color(self) -> str:
        """Returns the color of the vertex."""
        return self.__default_attributes.color

    def get_predecessor(self) -> 'Vertex | None':
        """Returns the predecessor of the vertex."""
        return self.__default_attributes.predecessor

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

    @validate_param_keyword(DefaultVertexType.__annotations__.keys())
    def update_default_attributes(self, **kwargs: Unpack[DefaultVertexType]):
        """
        Updates the default properties of the vertex, including:\n
        - Label
        - Color
        - Predecessor
        """
        self.__update(self.__default_attributes, **kwargs)

    @validate_param_keyword(BFSVertexType.__annotations__.keys())
    def update_bfs_attributes(self, **kwargs: Unpack[BFSVertexType]):
        """
        Updates BFS-specific attributes of the vertex, including:
        - Distance
        """
        self.__update(self.__special_attributes, **kwargs)

    @validate_param_keyword(DFSVertexType.__annotations__.keys())
    def update_dfs_attributes(self, **kwargs: Unpack[DFSVertexType]):
        """
        Updates DFS-specific attributes of the vertex.
        - Discovery Time
        - Finish Time
        """
        self.__update(self.__special_attributes, **kwargs)

    @validate_param_keyword(DijkstraVertexType.__annotations__.keys())
    def update_dijkstra_attributes(self, **kwargs: Unpack[DijkstraVertexType]):
        """
        Updates Dijkstra-specific attributes of the vertex.
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

    def get_neighbors(self) -> list['Vertex']:
        """Returns a list of neighboring vertices. Used specifically when traversing the graph."""
        return [edge.get_destination() for edge in self.__edges]

    # -------------------------------------------------------------------------------
    # END
    # -------------------------------------------------------------------------------

@dataclass
class DefaultEdgeAttributes:
    """A dataclass that's related to default attributes in an edge."""
    source: Vertex
    destination: Vertex

@dataclass
class SpecialEdgeAttributes:
    """A dataclass that specifies attributes when working with the edge."""
    weight: int
    classification: str | None = None

class Edge:
    """A class representing an edge in a graph."""

    def __init__(self, source: Vertex, destination: Vertex, weight: int = 1):
        self.__default_attributes: DefaultEdgeAttributes = DefaultEdgeAttributes(
            source=source,
            destination=destination
        )

        self.__special_attributes: SpecialEdgeAttributes = SpecialEdgeAttributes(weight)

    def __repr__(self) -> str:
        """Returns a string representation of the edge."""
        s = f"Edge({self.__default_attributes.source.get_label()}"
        s += f", {self.__default_attributes.destination.get_label()}"
        s += ')'

        return s

    # -------------------------------------------------------------------------------
    # List of getter functions to all attributes of an edge
    # -------------------------------------------------------------------------------

    def get_source(self) -> Vertex:
        """Returns the source vertex of an edge."""
        return self.__default_attributes.source

    def get_destination(self) -> Vertex:
        """Returns the destination vertex of an edge."""
        return self.__default_attributes.destination

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

    @validate_param_keyword(DefaultEdgeType.__annotations__.keys())
    def update_default_attributes(self, **kwargs: Unpack[DefaultEdgeType]):
        """
        Updates the properties of an edge, including:
        - Weight
        """
        self.__update(self.__default_attributes, **kwargs)

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
