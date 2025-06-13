"""A module help to validate the static typing in the edge object."""

from typing import TypedDict

class DefaultEdgeType(TypedDict, total=False):
    """A TypedDict for default edge attributes"""
    weight: int

class DFSEdgeType(TypedDict, total=False):
    """A TypedDict for DFS edge attributes"""
    classification: str | None
