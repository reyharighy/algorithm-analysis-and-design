"""A module help to validate the static typing in the vertex object."""

from typing import TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from tools.api.object import Vertex

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

class DijkstraVertexType(TypedDict, total=False):
    """A TypedDict for Dijkstra vertex attributes."""
    distance: int | float

class PrimVertexType(TypedDict, total=False):
    """A TypedDict for Prim's algorithm vertex attributes."""
    key: int | float

class KruskalVertexType(TypedDict, total=False):
    """A TypedDict for Kruskal's algorithm vertex attributes."""
    rank: int
