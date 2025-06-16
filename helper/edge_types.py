"""A module help to validate the static typing in the edge object."""

from typing import TypedDict

class DFSEdgeType(TypedDict, total=False):
    """A TypedDict for DFS edge attributes"""
    classification: str | None
