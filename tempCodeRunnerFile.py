G = nx.MultiDiGraph()
        for vertex in self.graph._get_vertices():
            label = vertex.get_label()
            dist = vertex.get_dijkstra_distance()
            G.add_node(label, label=f"{label}\n{dist}")

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

        # Loop khusus untuk menggambar edge bolak-balik
        drawn_edges = set()
        for u, v, data in G.edges(data=True):
            weight = data['weight']

            # Tentukan radius lengkungan
            if (v, u) in drawn_edges:
                rad = -0.25  # lawan arah, radius berlawanan
            elif (u, v) in drawn_edges:
                rad = 0.25
            else:
                rad = 0.1 if (v, u) in G.edges else 0.0

            drawn_edges.add((u, v))

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

            nx.draw_networkx_edge_labels(
                G,
                pos,
                edge_labels={(u, v): weight},
                font_size=10,
                label_pos=0.5
            )

        plt.title("Graph Visualization (Dijkstra)")
        plt.axis('off')
        plt.tight_layout()
        plt.show()