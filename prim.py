"""Module implementing Prim's algorithm for finding the minimum spanning tree of a graph."""
from graph import Graph
from object import Edge
import heapq
import itertools

def prim(graph: Graph, start_label: str = 'A') -> list[Edge]:
    # Prim's algorithm to find the minimum spanning tree (MST) of a graph.
    vertices = graph._get_vertices()
    if not vertices:
        return []

    mst_edges: list[Edge] = []
    visited: set[str] = set()
    edge_candidates: list[tuple[int, int, Edge]] = []

    counter = itertools.count()
    start = graph._get_vertex(start_label)

    if not start:
        raise ValueError(f"Start vertex '{start_label}' not found in graph")

    visited.add(start.get_label())

    for edge in start.get_edges():
        heapq.heappush(edge_candidates, (edge.get_weight(), next(counter), edge))

    while edge_candidates:
        _, _, edge = heapq.heappop(edge_candidates)
        dest_label = edge.get_destination().get_label()

        if dest_label in visited:
            continue

        mst_edges.append(edge)
        visited.add(dest_label)

        for next_edge in edge.get_destination().get_edges():
            next_dest_label = next_edge.get_destination().get_label()
            if next_dest_label not in visited:
                heapq.heappush(edge_candidates, (next_edge.get_weight(), next(counter), next_edge))

    return mst_edges