"""This module defines objects used in graph representation, including Vertex and Edge classes."""

from typing import TypedDict, Unpack
from dataclasses import dataclass
from validators import validate_labels, validate_keyword_params

class DefaultVertexType(TypedDict, total=False):
    """A TypedDict for default vertex attributes."""
    label: str
    color: str
    predecessor: 'Vertex | None'

class BFSVertexType(TypedDict, total=False):
    """A TypedDict for BFS vertex attributes."""
    distance: int | float

class DFSVertexType(TypedDict, total=False):
    """A TypedDict for DFS vertex attributes."""
    discovery_time: int | float
    finish_time: int | float

@dataclass
class BFSVertexAttributes:
    """A dataclass for BFS vertex attributes."""
    distance: int | float = float('inf')

@dataclass
class DFSVertexAttributes:
    """A dataclass for DFS vertex attributes."""
    discovery_time: int | float = 0
    finish_time: int | float = 0

class Vertex:
    """A class representing a vertex in a graph."""

    @validate_labels('label')
    def __init__(self, label: str):
        # Default attributes in Basic Graph
        self.__label: str = label
        self.__color: str = 'white'
        self.__predecessor: 'Vertex | None' = None
        self.__edges: list[Edge] = []

        # BFS-specific attributes
        self.__bfs_vertex_attributes: BFSVertexAttributes = BFSVertexAttributes()

        # DFS-specific attributes
        self.__dfs_vertex_attributes: DFSVertexAttributes = DFSVertexAttributes()

    def __repr__(self) -> str:
        """Returns a string representation of the vertex."""
        s = "Vertex({"
        s += f"label: {self.__label}"
        s += f", color: '{self.__color}'"
        s += ", predecessor: "

        if self.__predecessor:
            s += f"Vertex({self.__predecessor.get_label()})"
        else:
            s += "None"

        s += f", edges: {self.__edges}"
        s += "})"

        return s

    # -------------------------------------------------------------------------------
    # List of getter functions to all attributes of a vertex
    # -------------------------------------------------------------------------------

    def get_label(self) -> str:
        """Returns the label of the vertex."""
        return self.__label

    def get_color(self) -> str:
        """Returns the color of the vertex."""
        return self.__color

    def get_predecessor(self) -> 'Vertex | None':
        """Returns the predecessor of the vertex."""
        return self.__predecessor

    def get_edges(self) -> list['Edge']:
        """Returns a list of edges connected to the vertex."""
        return self.__edges

    def get_distance(self) -> int | float:
        """Returns the BFS distance of the vertex."""
        return self.__bfs_vertex_attributes.distance

    def get_discovery_time(self) -> int | float:
        """Returns the DFS discovery time of the vertex."""
        return self.__dfs_vertex_attributes.discovery_time

    def get_finish_time(self) -> int | float:
        """Returns the DFS finish time of the vertex."""
        return self.__dfs_vertex_attributes.finish_time

    # -------------------------------------------------------------------------------
    # END
    # -------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------
    # List of setter functions to all attributes of a vertex, except edge.
    # Edge should only be modified directly in the Edge class.
    # -------------------------------------------------------------------------------

    def update(self, this, **kwargs):
        """Update after successfull validation of parameter input"""
        for key, value in kwargs.items():
            if isinstance(this, Vertex):
                key = f"_{self.__class__.__name__}__{key}"

            if hasattr(this, key):
                setattr(this, key, value)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")

    @validate_keyword_params(DefaultVertexType.__annotations__.keys())
    def update_default_attributes(self, **kwargs: Unpack[DefaultVertexType]):
        """Updates the properties of the vertex."""
        self.update(self, **kwargs)

    @validate_keyword_params(BFSVertexType.__annotations__.keys())
    def update_bfs_attributes(self, **kwargs: Unpack[BFSVertexType]):
        """Updates BFS-specific attributes of the vertex."""
        self.update(self.__bfs_vertex_attributes, **kwargs)

    @validate_keyword_params(DFSVertexType.__annotations__.keys())
    def update_dfs_attributes(self, **kwargs: Unpack[DFSVertexType]):
        """Updates DFS-specific attributes of the vertex."""
        self.update(self.__dfs_vertex_attributes, **kwargs)

    # -------------------------------------------------------------------------------
    # END
    # -------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------
    # List of additional functions related to vertex when operating with graph
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

class DefaultEdgeType(TypedDict, total=False):
    """A TypedDict for default edge attributes"""
    weight: int

class DFSEdgeType(TypedDict, total=False):
    """A TypedDict for DFS edge attributes"""
    classification: str | None

@dataclass
class DFSEdgeAttributes:
    """A dataclass for DFS edge attributes"""
    classification: str | None = None

class Edge:
    """A class representing an edge in a graph."""

    def __init__(self, source: Vertex, destination: Vertex, weight: int = 1):
        self.__source: Vertex = source
        self.__destination: Vertex = destination
        self.__weight: int = weight

        # DFS-specific attributes
        self.__dfs_edge_attributes: DFSEdgeAttributes = DFSEdgeAttributes()

    def __repr__(self) -> str:
        """Returns a string representation of the edge."""
        s = f"Edge({self.__source.get_label()}"
        s += f", {self.__destination.get_label()}"
        s += f", {self.__weight})"

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
        return self.__weight

    def get_classification(self) -> str | None:
        """Returns the classification of an edge when running DFS."""
        return self.__dfs_edge_attributes.classification

    # -------------------------------------------------------------------------------
    # END
    # -------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------
    # List of setter functions to all attributes of an edge, except the source and
    # the destination vertices. They should only be modified directly in the vertex
    # class.
    # -------------------------------------------------------------------------------

    @validate_keyword_params(DefaultEdgeType.__annotations__.keys())
    def update_default_attributes(self, **kwargs: Unpack[DefaultEdgeType]):
        """Updates the properties of an edge."""
        if "__source" in kwargs:
            raise ValueError("Cannot update source directly")

        if "__destination" in kwargs:
            raise ValueError("Cannot update destination directly")

        for key, value in kwargs.items():
            attribute_key = f"_{self.__class__.__name__}__{key}"

            if hasattr(self, attribute_key):
                setattr(self, attribute_key, value)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")

    @validate_keyword_params(DFSEdgeType.__annotations__.keys())
    def update_dfs_attributes(self, **kwargs: Unpack[DFSEdgeType]):
        """Updates DFS-specific attributes of the edge."""
        for key, value in kwargs.items():
            if hasattr(self.__dfs_edge_attributes, key):
                setattr(self.__dfs_edge_attributes, key, value)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")        

    # -------------------------------------------------------------------------------
    # END
    # -------------------------------------------------------------------------------
