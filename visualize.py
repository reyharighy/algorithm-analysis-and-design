"""Module to visualize Minimum Spanning Tree (MST) and Dijkstra's algorithm results using networkx and matplotlib."""
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from object import Edge
from graph import Graph

def visualize_mst(mst_edges: list[Edge], title="Minimum Spanning Tree"):
    G = nx.Graph()

    for edge in mst_edges:
        u = edge.get_source().get_label()
        v = edge.get_destination().get_label()
        w = edge.get_weight()
        G.add_edge(u, v, weight=w)

    pos = {
        'A': (0, 0),
        'B': (8, 0),
        'C': (1, 1),
        'D': (2, 0),
        'E': (1, -1),
        'F': (3, 0),
        'G': (3, -1),
        'H': (5, -1),
        'I': (7, -0.5),
        'J': (6, 1),
        'K': (4, 1),
    }
    weights = nx.get_edge_attributes(G, 'weight')

    fig = plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_color='red')
    fig.suptitle(title, fontsize=14, y=0.95)
    plt.axis('off')
    fig.subplots_adjust(top=0.9)
    plt.show()

def visualize_dijkstra(graph: Graph):
    """Visualize the graph with Dijkstra distances using networkx and matplotlib."""

    G = nx.MultiDiGraph()

    for vertex in graph._get_vertices():
        label = vertex.get_label()
        dist = vertex.get_dijkstra_distance()
        display_dist = int(dist) if dist != float('inf') else '∞'
        G.add_node(label, label=f"{label}\n{display_dist}")

    for edge in graph._get_edges():
        src = edge.get_source().get_label()
        dst = edge.get_destination().get_label()
        weight = edge.get_weight()
        G.add_edge(src, dst, weight=weight)

    pos = {
        'S': (0, 0),
        'U': (1, 2),
        'X': (1, -2),
        'V': (3, 2),
        'Y': (3, -2),
    }

    node_labels = {n: G.nodes[n]['label'] for n in G.nodes}
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1500)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10)

    curve_rad = 0.25

    for u, v in G.edges():
        rad = 0
        if G.has_edge(v, u):
            rad = curve_rad

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=[(u, v)],
            connectionstyle=f"arc3,rad={rad}",
            arrowstyle="-|>",
            arrowsize=20,
            edge_color="black",
            width=2,
            min_source_margin=20,
            min_target_margin=20,
        )

    edge_weights = nx.get_edge_attributes(G, 'weight')
    for edge, weight in edge_weights.items():
        u, v, _ = edge
        is_curved = G.has_edge(v, u)

        pos_u = np.array(pos[u])
        pos_v = np.array(pos[v])
        vec = pos_v - pos_u
        angle = np.degrees(np.arctan2(vec[1], vec[0]))

        if angle > 90:
            angle -= 180
        if angle < -90:
            angle += 180

        label_pos = (pos_u + pos_v) / 2

        if is_curved:
            dist = np.linalg.norm(vec)
            if dist == 0: continue
            norm_vec = np.array([-vec[1], vec[0]])
            norm_vec_normalized = norm_vec / np.linalg.norm(norm_vec)
            midpoint = (pos_u + pos_v) / 2
            label_offset_factor = -0.3 
            label_pos = midpoint + label_offset_factor * norm_vec_normalized * curve_rad * dist

        plt.text(label_pos[0], label_pos[1], str(weight),
                 ha='center', va='center',
                 fontsize=9,
                 rotation=angle,
                 rotation_mode='anchor',
                 bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=0.1))

    plt.title("Graph Visualization (Dijkstra)")
    plt.axis('off')
    plt.tight_layout()
    plt.show()