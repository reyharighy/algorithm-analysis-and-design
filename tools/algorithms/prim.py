"""Module implementing Prim's algorithm for finding the minimum spanning tree of a graph."""
from tools.api.graph import Graph
from tools.api.object import Edge
import heapq
import itertools

def prim(graph: Graph, start_label: str = 'A') -> list[Edge]:
    mst_edges: list[Edge] = []
    visited: set[str] = set()
    edge_candidates: list[tuple[int, int, Edge]] = []
    counter = itertools.count()

    start_vertex = graph._get_vertex(start_label)
    if not start_vertex:
        raise ValueError(f"Start vertex '{start_label}' not found in graph")

    # Mark the starting vertex as visited and add its edges to the priority queue
    visited.add(start_vertex.get_label())
    for edge in start_vertex.get_edges():
        heapq.heappush(edge_candidates, (edge.get_weight(), next(counter), edge))

    # Loop until the priority queue is empty
    while edge_candidates:
        weight, _, edge = heapq.heappop(edge_candidates)
        destination = edge.get_destination()
        dest_label = destination.get_label()

        if dest_label not in visited:
            # Add the new vertex to the visited set
            visited.add(dest_label)
            # Add the edge to the MST
            mst_edges.append(edge)

            # Add all outgoing edges from the new vertex to the priority queue
            for next_edge in destination.get_edges():
                if next_edge.get_destination().get_label() not in visited:
                    heapq.heappush(edge_candidates, (next_edge.get_weight(), next(counter), next_edge))

    return mst_edges