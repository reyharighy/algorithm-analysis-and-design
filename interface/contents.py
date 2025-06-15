"""A module provides contents of the user-interaction program"""

MAIN_MENU = """\tPlease input an option number below:
\t  1. Breadth-First
\t  2. Depth-First
\t  3. Kruskal
\t  4. Prim
\t  5. Dijkstra
\t  6. Exit"""

BFS_MENU = """\tPlease input an option number below:
\t  1. Check graph vertices
\t  2. Create a dedicated graph from problem statement
\t  6. Back to main menu"""

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
