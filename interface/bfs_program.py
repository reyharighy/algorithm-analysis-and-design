"""Module to simulate user interaction with BFS algorithm"""

from interface.base_program import BaseProgram
from interface.contents import content_dictionary, TWO_DIRECTION_EDGE
from tools.algorithms.breadth_first_search import BreadthFirstSearch
from tools.api.object import Vertex

class BFSProgram(BaseProgram):
    """A class to provide a BFS-related operations to user."""

    def __init__(self) -> None:
        super().__init__()
        self.__bfs = BreadthFirstSearch()
        self._append_success_message(f"Activate subprogram: {self.__repr__()}")

    def __repr__(self) -> str:
        return "Breadth-First Search"

    def start(self):
        """A section to start the BFS program."""
        while True:
            self._clear_screen()

            content = content_dictionary['bfs']
            body = self.__bfs.definition('bfs') + content['body']
            self._display_content(content['title'], body)

            self._flush_session_message()
            option_input = self._option_entry_handler()
            self._loading()

            self._clear_screen()

            error_message = ''

            match option_input:
                case 1:
                    self.__create_vertex()
                    self._reset_sub_process()
                    continue
                case 2:
                    self.__create_edge()
                    self._reset_sub_process()
                    continue
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    self.__bfs.create_graph_from_problem_statement(1)
                    self._append_success_message("Graph has successfully been created")
                    continue
                case 6:
                    break
                case None:
                    error_message = "Invalid input: Input must not be empty"
                case -1:
                    error_message = "Invalid input: Only accept numeric type"
                case _:
                    error_message = f"Invalid input: No option number {option_input}"

            self._append_error_message(error_message)

    def save_exit(self):
        """Save configuration made after exiting the program."""

    def __create_vertex(self):
        """Simulate a process of adding a new vertex."""
        title: str = " CREATE A NEW VERTEX "
        body: str = self.__bfs.definition('bfs')

        while True:
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
                else:
                    self._append_error_message(f"Vertex({label_input}) already exists")

                break

    def __edge_exists(self, source: Vertex, destination: Vertex) -> bool:
        """Checkes if such edge exists."""
        for edge in source.get_edges():
            if edge.get_destination() is destination:
                return True

        return False

    def __edge_complement_exists(self, source: Vertex, destination: Vertex) -> bool:
        """Checkes if there's a complement of such edge."""
        for edge in destination.get_edges():
            if edge.get_destination() is source:
                return True

        return False

    def __create_edge_content(self, src: Vertex | None, dest: Vertex | None, valid: bool) -> str:
        """Provides a customized content when adding a new edge."""
        body: str = self.__bfs.definition('bfs')
        source_definition = None
        destination_definition = None

        if isinstance(src, Vertex):
            source_definition = src.definition('bfs')

        source_prompt: str = '\n' + f"\tSource:\n\t  - {source_definition}"
        body += source_prompt

        if isinstance(dest, Vertex):
            destination_definition = dest.definition('bfs')

        destination_prompt: str = '\n' + f"\tDestination:\n\t  - {destination_definition}"
        body += destination_prompt + '\n'

        if isinstance(src, Vertex) and isinstance(dest, Vertex) and valid:
            if not self.__edge_complement_exists(src, dest):
                body += TWO_DIRECTION_EDGE

        return body

    def __get_vertex_session(self, search_for: str) -> Vertex | None:
        """Provides a message session when finding a vertex."""
        label_input = input(f"Enter {search_for} vertex label: ")
        self._loading()

        vertex = self.__bfs.get_vertex(label_input)

        if isinstance(vertex, str):
            self._append_error_message(str(vertex))
        elif vertex is None:
            self._append_error_message(f"Invalid: Vertex({label_input}) is not found")
        else:
            self._append_success_message(f"Vertex({label_input}) is found")
            return vertex

        return None

    def __create_edge_session(self, source: Vertex, destination: Vertex, two_direction: bool):
        """Provides a message upon successfull edge creation."""
        if two_direction:
            edge_label_1 = f"Edge({source.get_label()}, {destination.get_label()})"
            edge_label_2 = f"Edge({destination.get_label()}, {source.get_label()})"
            edge_label = f"{edge_label_1} and {edge_label_2}"
            self._append_success_message(f"{edge_label} have successfully been created")
            return

        edge_label = f"Edge({source.get_label()}, {destination.get_label()})"
        self._append_success_message(f"{edge_label} has successfully been created")

    def __create_edge(self):
        """Simulate a process of adding a new edge."""
        if len(self.__bfs.get_vertices()) < 2:
            self._append_error_message("Invalid: Graph must contain at least two vertices")
            return

        title: str = " CREATE A NEW EDGE "
        source: Vertex | None = None
        destination: Vertex | None = None

        while True:
            self._clear_screen()

            body = self.__create_edge_content(source, destination, self._sub.valid)
            self._display_content(title, body)

            self._flush_session_message()

            if source is None:
                source = self.__get_vertex_session("source")

            elif destination is None:
                destination = self.__get_vertex_session("destination")

            elif source and destination and not self._sub.valid:
                if self.__edge_exists(source, destination):
                    src_label, dest_label = source.get_label(), destination.get_label()
                    error_message = f"Invalid: Edge({src_label}, {dest_label}) already exists"
                    self._append_error_message(error_message)
                    break

                self._sub.valid = True

            elif self._sub.valid:
                if self.__edge_complement_exists(source, destination):
                    self.__bfs.add_edge(source, destination)
                    break

                option_input = self._option_entry_handler()
                self._loading()
                error_message = ''

                match option_input:
                    case 1:
                        self.__bfs.add_edge(source, destination)
                        break
                    case 2:
                        self.__bfs.add_edge(source, destination, (1, 1))
                        self._sub.two_direction = True
                        break
                    case None:
                        error_message = "Invalid input: Input must not be empty"
                    case -1:
                        error_message = "Invalid input: Only accept numeric type"
                    case _:
                        error_message = f"Invalid input: No option number {option_input}"

                self._append_error_message(error_message)

        if self._sub.valid:
            self.__create_edge_session(source, destination, self._sub.two_direction)
