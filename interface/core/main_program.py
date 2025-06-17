"""Entry point for the user to use the program interactively."""

from interface.core.base_program import BaseProgram
from interface.sub.bfs_program import BFSProgram
from interface.sub.dfs_program import DFSProgram
from interface.sub.dijkstra_program import DijkstraProgram
from interface.sub.kruskal_program import KruskalProgram
from interface.sub.prim_program import PrimProgram
from interface.contents import content_dictionary

class MainProgram(BaseProgram):
    """A class to provide an interface of the main program."""

    def __init__(self) -> None:
        super().__init__()
        self.__running_program = None

    def __execute_subprogram(self):
        """Executes a process depending on the user input."""
        option_input = self._option_entry_handler()

        match option_input:
            case 1:
                self.__running_program = BFSProgram()
                self.__cycle()
                return
            case 2:
                self.__running_program = DFSProgram()
                self.__cycle()
                return
            case 3:
                self.__running_program = KruskalProgram()
                self.__cycle()
                return
            case 4:
                self.__running_program = PrimProgram()
                self.__cycle()
                return
            case 5:
                self.__running_program = DijkstraProgram()
                self.__cycle()
                return
            case 6:
                self._extrn.resume = False
                self._append_success_message("\nExited")
                return
            case None:
                self._base.message = "Invalid: Input must not be empty"
            case -1:
                self._base.message = "Invalid: Only accepts numerics without spaces in between"
            case _:
                self._base.message = f"Invalid: No option number {option_input}"

        self._append_error_message(self._base.message)

    def start(self):
        """A section to start the main program."""
        content = content_dictionary['main_menu']
        title = content['title']
        body = content['body']

        while self._extrn.resume:
            self._refresh_display(title, body)
            self.__execute_subprogram()

        self._close_program()

    def save_exit(self):
        """Saves configuration made after exiting the program."""

    def deactivate_running_program(self):
        """Kills the process of running program."""
        self._append_success_message(f"Deactivate subprogram: {self.__running_program}")
        self.__running_program = None

    def __cycle(self):
        """Runs the subprogram in a cycle."""
        if self.__running_program:
            self.__running_program.start()
            self.__running_program.save_exit()

        self.deactivate_running_program()
