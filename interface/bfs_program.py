"""Module to simulate user interaction with BFS algorithm"""

from interface.base_program import BaseProgram
from interface.contents import content_dictionary
from tools.algorithms.breadth_first_search import BreadthFirstSearch
from tools.api.object import Vertex

class BFSProgram(BaseProgram):
    """A class to provide a BFS-related operations to user."""

    def __init__(self) -> None:
        super().__init__()
        self._append_success_message(f"Activate subprogram: {self.__repr__()}")
        self.__bfs = BreadthFirstSearch()

    def __repr__(self) -> str:
        return "Breadth-First Search"

    def start(self):
        """A section to start the BFS program."""
        while not self._terminate:
            self._clear_screen()

            content = content_dictionary['bfs']
            body = self.__bfs.graph_definition('bfs') + content['body']
            self._display_content(content['title'], body)

            self._flush_session_message()
            option_input = self._option_entry_handler()
            self._loading()

            self._clear_screen()

            match option_input:
                case 1:
                    self.__create_a_vertex()
                case 2:
                    self.__create_an_edge()
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    self.__bfs.create_graph_from_problem_statement(1)
                    self._append_success_message("Graph has been successfully created")
                case 6:
                    self._terminate = True
                case None:
                    self._append_error_message("Invalid input: Input must not be empty")
                case -1:
                    self._append_error_message("Invalid input: Only accept numeric type")
                case _:
                    self._append_error_message(f"Invalid input: No option number {option_input}")

    def save_exit(self):
        """Save configuration made after exiting the program."""

    def __create_a_vertex(self):
        """Simulate a process of adding a new vertex."""
        title: str = " CREATE A NEW VERTEX "
        body: str = self.__bfs.graph_definition('bfs')
        is_valid: bool = False

        while not is_valid:
            self._clear_screen()

            self._display_content(title, body)

            self._flush_session_message()
            label_input = input("Enter vertex label: ")
            self._loading()

            self._clear_screen()

            vertex = self.__bfs.add_vertex(label_input)

            if isinstance(vertex, str):
                self._append_error_message(str(vertex))
            else:
                if vertex:
                    self._append_success_message(f"Vertex({label_input}) has been created")
                    is_valid = True
                else:
                    self._append_error_message(f"Vertex({label_input}) already exists")

    def __create_an_edge(self):
        """Simulate a process of adding a new edge."""
        if len(self.__bfs.get_vertices()) < 2:
            self._append_error_message("Invalid: Graph must contain at least two vertices")
            return

        title: str = " CREATE A NEW EDGE "
        body: str = ""
        is_valid: bool = False

        src_vertex: Vertex | None = None
        dest_vertex: Vertex | None = None

        while not is_valid:
            self._clear_screen()

            chosen_source = f"\tSource = {src_vertex if src_vertex else "undefined"}"
            source_prompt: str = '\n\n' + chosen_source
            body += source_prompt

            chosen_destination = f"\tDestination = {dest_vertex if dest_vertex else "undefined"}"
            destination_prompt: str = '\n' + chosen_destination
            body += destination_prompt

            self._display_content(title, body)

            self._flush_session_message()
