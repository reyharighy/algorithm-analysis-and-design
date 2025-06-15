"""Entry point for the user to use the program interactively."""

from interface.base_program import BaseProgram
from interface.bfs_program import BFSProgram
from interface.contents import content_dictionary

class MainProgram(BaseProgram):
    """A class to provide an interface of the main program."""

    def __init__(self) -> None:
        super().__init__()
        self.__running_program = None

    def start(self):
        """A section to start the main program."""
        while True:
            self._clear_screen()

            content = content_dictionary['main_menu']
            self._display_content(content['title'], content['body'])

            self._flush_session_message()
            option_input = self._option_entry_handler()
            self._loading()

            self._clear_screen()

            error_message = ''

            match option_input:
                case 1:
                    self.__running_program = BFSProgram()
                    self.__running_program.start()
                    self.__running_program.save_exit()
                    self.deactivate_running_program()
                    continue
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    break
                case None:
                    error_message = "Invalid: Input must not be empty"
                case -1:
                    error_message = "Invalid: Only accepts numerics without spaces in between"
                case _:
                    error_message = f"Invalid: No option number {option_input}"

            self._append_error_message(error_message)

    def save_exit(self):
        """Save configuration made after exiting the program."""

    def deactivate_running_program(self):
        """Kill the process of running program."""
        self._append_success_message(f"Deactivate subprogram: {self.__running_program}")
        self.__running_program = None
