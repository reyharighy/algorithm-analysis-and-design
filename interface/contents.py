"""A module provides contents of the user-interaction program"""

MAIN_MENU = """
\tPlease input an option number below:
\t  1. Breadth-First Search
\t  2. Depth-First Search
\t  3. Kruskal
\t  4. Prim
\t  5. Dijkstra
\t  6. Exit
"""

BFS_MENU = """
\tPlease input an option number below:
\t  1. Create a new vertex
\t  2. Create a new edge
\t  5. Create a dedicated graph
\t  6. Back to main menu
"""

content_dictionary = {
    'main_menu': {
        'title': " MAIN MENU ",
        'body': MAIN_MENU
    },

    'bfs': {
        'title': " BREADTH-FIRST SEARCH ",
        'body': BFS_MENU
    }
}
