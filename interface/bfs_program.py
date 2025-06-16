"""Module to simulate user interaction with BFS algorithm"""

from interface.base_program import BaseProgram
from interface.contents import content_dictionary, subcontent_dictionary
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

    def __execute_process(self):
        """Execute the subprocess depending on the user input."""
        option_input = self._option_entry_handler()

        match option_input:
            case 1:
                self.__create_vertex()
                self._reset_contexts()
                return
            case 2:
                self.__create_edge()
                self._reset_contexts()
                return
            case 3:
                pass
            case 4:
                pass
            case 5:
                self.__bfs.create_graph_from_problem_statement(1)
                self._append_success_message("Graph has successfully been created")
                return
            case 6:
                self._sub.resume = False
                return
            case None:
                self._sub.message = "Invalid input: Input must not be empty"
            case -1:
                self._sub.message = "Invalid input: Only accept numeric type"
            case _:
                self._sub.message = f"Invalid input: No option number {option_input}"

        self._append_error_message(self._sub.message)

    def start(self):
        """A section to start the BFS program."""
        content = content_dictionary['bfs']
        title: str = content['title']
        body: str = content['body']

        while self._sub.resume:
            self._refresh_display(title, self.__bfs.definition('bfs') + body)
            self.__execute_process()

    def save_exit(self):
        """Save configuration made after exiting the program."""

    def __vertex_creation_session(self):
        """Provides a session when creating a vertex."""
        label_input = input("Enter vertex label: ")
        self._loading()

        vertex = self.__bfs.add_vertex(label_input)

        if isinstance(vertex, str):
            self._append_error_message(str(vertex))
        else:
            if vertex:
                self._append_success_message(f"Vertex({label_input}) has been created")
            else:
                self._append_error_message(f"Vertex({label_input}) already exists")

            self._sub.resume = False

    def __create_vertex(self):
        """Simulate a process of adding a new vertex."""
        title: str = " CREATE A NEW VERTEX "

        while self._sub.resume:
            self._refresh_display(title, self.__bfs.definition('bfs'))
            self.__vertex_creation_session()

    def __edge_complement_exists(self, source: Vertex, destination: Vertex) -> bool:
        """Checkes if there's a complement of such edge."""
        for edge in destination.get_edges():
            if edge.get_destination() is source:
                return True

        return False

    def __edge_creation_content(self, src: Vertex | None, dest: Vertex | None, valid: bool) -> str:
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
                body += subcontent_dictionary['two_direction_edge']

        return body

    def __vertex_retrieval_session(self, search_for: str) -> Vertex | None:
        """Provides a session when retrieving a vertex."""
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

    def __edge_exists(self, source: Vertex, destination: Vertex) -> bool:
        """Checks if such edge is valid"""
        for edge in source.get_edges():
            if edge.get_destination() is destination:
                src_label, dest_label = source.get_label(), destination.get_label()
                self._sub.message = f"Invalid: Edge({src_label}, {dest_label}) already exists"
                self._append_error_message(self._sub.message)
                self._sub.resume = False
                return True

        return False

    def __edge_creation_process(self, source: Vertex, destination: Vertex):
        """Execute a process of creating an edge upon successful validation."""
        if self.__edge_complement_exists(source, destination):
            self.__bfs.add_edge(source, destination)
            self._sub.resume = False
            self.__edge_creation_session(source, destination, self._sub.two_direction)
            return

        option_input = self._option_entry_handler()

        match option_input:
            case 1:
                self.__bfs.add_edge(source, destination)
                self._sub.resume = False
                self.__edge_creation_session(source, destination, self._sub.two_direction)
                return
            case 2:
                self.__bfs.add_edge(source, destination, (1, 1))
                self._sub.two_direction = True
                self._sub.resume = False
                self.__edge_creation_session(source, destination, self._sub.two_direction)
                return
            case None:
                self._sub.message = "Invalid input: Input must not be empty"
            case -1:
                self._sub.message = "Invalid input: Only accept numeric type"
            case _:
                self._sub.message = f"Invalid input: No option number {option_input}"

        self._append_error_message(self._sub.message)

    def __edge_creation_session(self, source: Vertex, destination: Vertex, two_direction: bool):
        """Provides a session when creating an edge."""
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

        while self._sub.resume:
            body = self.__edge_creation_content(source, destination, self._sub.valid)
            self._refresh_display(title, body)

            if source is None:
                source = self.__vertex_retrieval_session("source")

            elif destination is None:
                destination = self.__vertex_retrieval_session("destination")

            elif source and destination and not self._sub.valid:
                self._sub.valid = not self.__edge_exists(source, destination)

            elif self._sub.valid:
                self.__edge_creation_process(source, destination)
