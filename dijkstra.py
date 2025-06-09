"""Module that implements Dijkstra's algorithm using existing Graph structure."""
from graph import Graph
import heapq
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Dijkstra:
    def __init__(self):
        self.graph = Graph()

    def create_graph_from_problem_statement(self, task_number: int):
        self.graph.create_graph_from_problem_statement(task_number)

    def run(self, start_label: str):
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
        return self.graph._get_vertices()
    
    def visualize(self):
        """Visualize the graph using networkx and matplotlib."""

        G = nx.MultiDiGraph()
        for vertex in self.graph._get_vertices():
            label = vertex.get_label()
            dist = vertex.get_dijkstra_distance()
            display_dist = int(dist) if dist != float('inf') else '∞'
            G.add_node(label, label=f"{label}\n{display_dist}")

        for edge in self.graph._get_edges():
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

        # --- Start of suggested changes ---

        # Tetapkan nilai lengkungan yang konsisten untuk semua edge bolak-balik
        curve_rad = 0.25

        # 1. Gambar semua edge terlebih dahulu
        for u, v in G.edges():
            rad = 0
            # Jika ada edge balikan, gunakan nilai lengkungan yang sudah ditetapkan
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
                min_source_margin= 20,
                min_target_margin= 20,
            )
        
        # 2. Gambar label edge secara manual
        edge_weights = nx.get_edge_attributes(G, 'weight')
        for edge, weight in edge_weights.items():
            u, v, _ = edge
            
            is_curved = G.has_edge(v, u)
            
            pos_u = np.array(pos[u])
            pos_v = np.array(pos[v])
            
            # --- Start of New Logic for Position and Rotation ---
            
            # Hitung sudut kemiringan edge untuk rotasi label
            vec = pos_v - pos_u
            angle = np.degrees(np.arctan2(vec[1], vec[0]))
            
            # Logika untuk memastikan teks tidak terbalik (tetap upright)
            if angle > 90:
                angle -= 180
            if angle < -90:
                angle += 180

            # Hitung posisi label
            label_pos = (pos_u + pos_v) / 2  # Posisi default untuk edge lurus

            if is_curved:
                dist = np.linalg.norm(vec)
                if dist == 0: continue
                
                norm_vec = np.array([-vec[1], vec[0]])
                norm_vec_normalized = norm_vec / np.linalg.norm(norm_vec)
                
                midpoint = (pos_u + pos_v) / 2
                
                # Faktor pengali untuk mendorong label lebih dekat ke lengkungan
                label_offset_factor = -0.3 
                label_pos = midpoint + label_offset_factor * norm_vec_normalized * curve_rad * dist

            # Gunakan plt.text untuk menempatkan label, tambahkan parameter 'rotation'
            plt.text(label_pos[0], label_pos[1], str(weight),
                    ha='center', va='center',
                    fontsize=9,
                    rotation=angle,  # <-- Perubahan utama: tambahkan rotasi
                    rotation_mode='anchor', # <-- Pastikan rotasi sesuai
                    bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=0.1))

        # --- End of suggested changes ---

        plt.title("Graph Visualization (Dijkstra)")
        plt.axis('off')
        plt.tight_layout()
        plt.show()