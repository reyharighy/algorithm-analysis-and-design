"""This module defines objects used in graph representation, including Vertex and Edge classes."""

from typing import TypedDict, Unpack

class VertexAttributes(TypedDict, total=False):
    """A TypedDict for vertex attributes."""
    label: str
    predecessor: 'Vertex | None'
    distance: int | float
    visited: bool
    color: str

class Vertex:
    """A class representing a vertex in a graph."""

    def __init__(self, label: str):
        self.__label: str = label
        self.__edges: list[Edge] = []

        # Default attributes
        self.__predecessor: Vertex | None = None
        self.__distance: int | float = float('inf')
        self.__visited: bool = False
        self.__color: str = 'white'

    def __repr__(self) -> str:
        """Returns a string representation of the vertex."""
        s = "Vertex({"
        s += f"label: {self.__label}"
        s += ", predecessor: "

        if self.__predecessor:
            s += f"Vertex({self.__predecessor.get_label()})"
        else:
            s += "None"

        s += f", edges: {self.__edges}"
        s += f", distance: {self.__distance}"
        s += f", visited: {self.__visited}"
        s += f", color: '{self.__color}'"
        s += "})"

        return s

    def update_attributes(self, **kwargs: Unpack[VertexAttributes]):
        """Updates the properties of the vertex."""
        if '__edges' in kwargs:
            raise ValueError("Cannot update edges directly.")

        for key, value in kwargs.items():
            attribute_key = f"_{self.__class__.__name__}__{key}"

            if hasattr(self, attribute_key):
                setattr(self, attribute_key, value)

    def add_edge(self, edge: 'Edge'):
        """Adds an edge to the vertex."""
        self.__edges.append(edge)

    def get_label(self) -> str:
        """Returns the label of the vertex."""
        return self.__label

    def get_edges(self) -> list['Edge']:
        """Returns a list of edges connected to the vertex."""
        return self.__edges

    def get_color(self) -> str:
        """Returns the color of the vertex."""
        return self.__color

    def get_distance(self) -> int | float:
        """Returns the distance from the start vertex."""
        return self.__distance

    def get_neighbors(self) -> list['Vertex']:
        """Returns a list of neighboring vertices."""
        return [edge.destination for edge in self.__edges]

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
