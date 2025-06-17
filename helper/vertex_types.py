"""A module help to validate the static typing in the vertex object."""

from typing import TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from tools.api.object import Vertex

class BFSVertexType(TypedDict, total=False):
    """A TypedDict for BFS vertex attributes."""
    color: str
    predecessor: 'Vertex | None'
    distance: int | float

class DFSVertexType(TypedDict, total=False):
    """A TypedDict for DFS vertex attributes."""
    color: str
    predecessor: 'Vertex | None'
    discovery_time: int | float
    finish_time: int | float

class DijkstraVertexType(TypedDict, total=False):
    """A TypedDict for Dijkstra vertex attributes."""
    predecessor: 'Vertex | None'
    distance: int | float
