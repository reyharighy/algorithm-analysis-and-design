"""Module that implements Dijkstra's algorithm using existing Graph structure."""
from graph import Graph
import heapq
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Dijkstra:
    def __init__(self):
        # Initialize the Dijkstra algorithm with an empty graph
        self.graph = Graph()

    def create_graph_from_problem_statement(self, task_number: int):
        # Create a graph based on the problem statement for the given task number
        self.graph.create_graph_from_problem_statement(task_number)

    def run(self, start_label: str):
        # Run Dijkstra's algorithm starting from the vertex with the given label
        vertices = self.graph._get_vertices()
        start = self.graph._get_vertex(start_label)

        for v in vertices:
            v.set_dijkstra_distance(float('inf'))
        start.set_dijkstra_distance(0)

        pq = [(0, start)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > current_vertex.get_distance():
                continue

            for edge in current_vertex.get_edges():
                neighbor = edge.get_destination()
                weight = edge.get_weight()
                new_distance = current_distance + weight

                if new_distance < neighbor.get_dijkstra_distance():
                    neighbor.set_dijkstra_distance(new_distance)
                    heapq.heappush(pq, (new_distance, neighbor))

    def get_vertices(self):
        # Return the list of vertices in the graph
        return self.graph._get_vertices()