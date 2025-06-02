"""This module defines objects used in graph representation, including Vertex and Edge classes."""

from typing import TypedDict, Unpack

class VertexAttributes(TypedDict, total=False):
    """A TypedDict for vertex attributes."""
    label: str
    predecessor: 'Vertex | None'
    distance: int | float
    visited: bool

class Vertex:
    """A class representing a vertex in a graph."""

    def __init__(self, label: str):
        self.label: str = label
        self.predecessor: Vertex | None = None
        self.edges: list[Edge] = []
        self.distance: int | float = float('inf')
        self.visited: bool = False

    def __repr__(self) -> str:
        """Returns a string representation of the vertex."""
        s = "Vertex({"
        s += f"label: {self.label}"
        s += ", predecessor: "

        if self.predecessor:
            s += f"Vertex({self.predecessor.label})"
        else:
            s += "None"

        s += f", edges: {self.edges}"
        s += f", distance: {self.distance}"
        s += f", visited: {self.visited}"
        s += "})"

        return s

    def update_attributes(self, **kwargs: Unpack[VertexAttributes]):
        """Updates the properties of the vertex."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def add_edge(self, edge: 'Edge'):
        """Adds an edge to the vertex."""
        self.edges.append(edge)

    def get_neighbors(self) -> list['Vertex']:
        """Returns a list of neighboring vertices."""
        return [edge.destination for edge in self.edges]

class Edge:
    """A class representing an edge in a graph."""

    def __init__(self, source: Vertex, destination: Vertex, weight: int = 1):
        self.source: Vertex = source
        self.destination: Vertex = destination
        self.weight: int = weight

    def __repr__(self) -> str:
        """Returns a string representation of the edge."""
        return f"Edge({self.source.label}, {self.destination.label}, {self.weight})"

    def update_weight(self, new_weight: int):
        """Updates the weight of the edge."""
        if new_weight < 0:
            return

        self.weight = new_weight
