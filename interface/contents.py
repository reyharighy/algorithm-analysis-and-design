"""A module provides contents of the user-interaction program"""

MAIN_MENU = """
\tPlease input an option number below:
\t  1. BFS
\t  2. DFS
\t  3. Kruskal
\t  4. Prim
\t  5. Dijkstra
\t  6. Exit
"""

BFS_MENU = """
\tPlease input an option number below:
\t  1. Create new vertex
\t  2. Create new edge
\t  3. Create reserved graph
\t  4. Visualize graph
\t  5. Run BFS on graph
\t  6. Back to main menu
"""

DFS_MENU = """
\tPlease input an option number below:
\t  1. Create new vertex
\t  2. Create new edge
\t  3. Create reserved graph
\t  4. Visualize graph
\t  5. Run DFS on graph
\t  6. Back to main menu
"""

KRUSKAL_MENU = """
\tPlease input an option number below:
\t  1. Create new vertex
\t  2. Create new edge
\t  3. Create reserved graph
\t  4. Visualize graph
\t  5. Run Kruskal search on graph
\t  6. Back to main menu
"""

PRIM_MENU = """
\tPlease input an option number below:
\t  1. Create new vertex
\t  2. Create new edge
\t  3. Create reserved graph
\t  4. Visualize graph
\t  5. Run Prim search on graph
\t  6. Back to main menu
"""

DIJKSTRA_MENU = """
\tPlease input an option number below:
\t  1. Create new vertex
\t  2. Create new edge
\t  3. Create reserved graph
\t  4. Run Dijkstra search on graph
\t  5. Back to main menu
"""

content_dictionary = {
    'main_menu': {
        'title': " MAIN MENU ",
        'body': MAIN_MENU
    },

    'bfs': {
        'title': " BREADTH-FIRST SEARCH ",
        'body': BFS_MENU
    },

    'dfs': {
        'title': " DEPTH-FIRST SEARCH ",
        'body': DFS_MENU
    },

    'kruskal': {
        'title': " KRUSKAL SEARCH ",
        'body': KRUSKAL_MENU
    },

    'prim': {
        'title': " PRIM SEARCH ",
        'body': PRIM_MENU
    },

    'dijkstra': {
        'title': " DIJKSTRA SEARCH",
        'body': DIJKSTRA_MENU
    }
}

TWO_DIRECTION_EDGE = """
\tPlease input an option number below:
\t  1. One-direction Edge
\t  2. Two-direction Edge
"""

subcontent_dictionary = {
    'two_direction_edge' : TWO_DIRECTION_EDGE
}
