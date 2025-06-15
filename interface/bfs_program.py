"""Module to simulate user interaction with BFS algorithm"""

from interface.base_program import BaseProgram
from interface.contents import content_dictionary
from tools.algorithms.breadth_first_search import BreadthFirstSearch

class BFSProgram(BaseProgram):
    """A class to provide a BFS-related operations to user."""

    def __init__(self) -> None:
        super().__init__()
        self.__bfs = BreadthFirstSearch()

    def start(self):
        """A section to start the BFS program."""
        while not self._terminate:
            self._clear_screen()

            content = content_dictionary['bfs']
            self._display_content(content['title'], content['body'])

            print(f"{self._error_message}")
            option_input = self._option_entry_handler()
            self._loading()
            self._clear_screen()

            match option_input:
                case 1:
                    self.__check_graph()
                case 2:
                    self.__bfs.create_graph_from_problem_statement(1)
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    self._terminate = True
                case None:
                    self._error_message = 'Invalid input: Input must not be empty.'
                case -1:
                    self._error_message = "Invalid input: Only accept numeric type."
                case _:
                    self._error_message = f"Invalid input: No option number {option_input}."

    def save_exit(self):
        """Save configuration made after exiting the program."""

    def __check_graph(self):
        """Return the graph definition"""
        title = " DEPTH-FIRST SEARCH GRAPH DEFINITION "
        body: str | None = None

        if self.__bfs.get_vertices():
            for vertex in self.__bfs.get_vertices():
                print(vertex)
        else:
            body = "Graph is empty.".center(self._terminal_width, " ")

        if body:
            self._display_content(title, body, margin=5)

        input("Put any key to continue")
        self._loading()
