"""This module defines objects used in graph representation, including Vertex and Edge classes."""

from typing import TypedDict, Unpack
from dataclasses import dataclass
from validators import validate_labels

class VertexDefaultAttributes(TypedDict, total=False):
    """A TypedDict for vertex attributes."""
    label: str
    color: str
    predecessor: 'Vertex | None'

class BFSUniqueAttributes(TypedDict, total=False):
    """A TypedDict for BFS unique attributes."""
    distance: int | float

class DFSUniqueAttributes(TypedDict, total=False):
    """A TypedDict for DFS unique attributes."""
    discovery_time: int | float
    finish_time: int | float

@dataclass
class BFSAttributes:
    """A dataclass for BFS attributes."""
    distance: int | float = float('inf')

@dataclass
class DFSAttributes:
    """A dataclass for DFS attributes."""
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
        self.__bfs_attributes: BFSAttributes = BFSAttributes()

        # DFS-specific attributes
        self.__dfs_attributes: DFSAttributes = DFSAttributes()

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

    def add_edge(self, edge: 'Edge'):
        """Adds an edge to the vertex."""
        self.__edges.append(edge)

    def get_label(self) -> str:
        """Returns the label of the vertex."""
        return self.__label

    def get_edges(self) -> list['Edge']:
        """Returns a list of edges connected to the vertex."""
        return self.__edges

    def get_predecessor(self) -> 'Vertex | None':
        """Returns the predecessor of the vertex."""
        return self.__predecessor

    def get_color(self) -> str:
        """Returns the color of the vertex."""
        return self.__color

    def get_neighbors(self) -> list['Vertex']:
        """Returns a list of neighboring vertices. Used specifically when traversing the graph."""
        return [edge.destination for edge in self.__edges]

    def get_distance(self) -> int | float:
        """Returns the BFS distance of the vertex."""
        return self.__bfs_attributes.distance

    def get_discovery_time(self) -> int | float:
        """Returns the DFS discovery time of the vertex."""
        return self.__dfs_attributes.discovery_time

    def get_finish_time(self) -> int | float:
        """Returns the DFS finish time of the vertex."""
        return self.__dfs_attributes.finish_time

    def update_default_attributes(self, **kwargs: Unpack[VertexDefaultAttributes]):
        """Updates the properties of the vertex."""
        if '__edges' in kwargs:
            raise ValueError("Cannot update edges directly.")

        for key, value in kwargs.items():
            attribute_key = f"_{self.__class__.__name__}__{key}"

            if hasattr(self, attribute_key):
                setattr(self, attribute_key, value)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")

    def update_bfs_attributes(self, **kwargs: Unpack[BFSUniqueAttributes]):
        """Updates BFS-specific attributes of the vertex."""
        for key, value in kwargs.items():
            if hasattr(self.__bfs_attributes, key):
                setattr(self.__bfs_attributes, key, value)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")

    def update_dfs_attributes(self, **kwargs: Unpack[DFSUniqueAttributes]):
        """Updates DFS-specific attributes of the vertex."""
        for key, value in kwargs.items():
            if hasattr(self.__dfs_attributes, key):
                setattr(self.__dfs_attributes, key, value)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")

class Edge:
    """A class representing an edge in a graph."""

    def __init__(self, source: Vertex, destination: Vertex, weight: int = 1):
        self.source: Vertex = source
        self.destination: Vertex = destination
        self.weight: int = weight

    def __repr__(self) -> str:
        """Returns a string representation of the edge."""
        return f"Edge({self.source.get_label()}, {self.destination.get_label()}, {self.weight})"

    def update_weight(self, new_weight: int):
        """Updates the weight of the edge."""
        if new_weight < 0:
            raise ValueError("Weight cannot be negative.")

        self.weight = new_weight
