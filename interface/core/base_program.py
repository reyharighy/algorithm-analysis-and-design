"""A module to provide shared funtionality accross all programs"""

import os
import time
import threading
from sys import stdout
from dataclasses import dataclass, field
from rich import print as session

@dataclass
class Base:
    """A class to provide general status dedicated to internal running process."""
    message: str = ''
    animated: bool = False
    success = True

@dataclass
class External:
    """A class to provide general status dedicated to external running process."""
    resume: bool = True
    valid: bool = False

@dataclass
class GraphProcess:
    """A class to provide context indicating if a graph is already run."""
    run: bool = False

@dataclass
class EdgeProcess:
    """A class to provide context dedicated to a process of defining the edge's weight."""
    two_direction: bool = False
    weight: bool = False
    int_weight: bool = False
    first_weight: bool = False
    second_weight: bool = False
    weight_list: list[int] = field(default_factory=list)

class BaseProgram:
    """A class to provide basic operation when using a program."""

    def __init__(self) -> None:
        self._terminal_height: int = int(os.popen('stty size', 'r').read().split()[0])
        self._terminal_width: int = int(os.popen('stty size', 'r').read().split()[1])

        self._base: Base = Base()
        self._extrn: External = External()
        self._edg: EdgeProcess = EdgeProcess()
        self._grph: GraphProcess = GraphProcess()

    def start(self):
        """Not implemented."""

    def save_exit(self):
        """Not implemented."""

    def _close_program(self):
        """Kills the main program."""
        self._flush_session_message()
        self._loading()
        self._clear_screen()

    def _clear_screen(self):
        """Refreshes the screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def __header(self, name: str) -> str:
        """Prints a header."""
        s = "".center(self._terminal_width, '=') + '\n\n'
        s += f"{name}".center(self._terminal_width, ' ') + '\n'
        s += '\n' + "".center(self._terminal_width, '=')

        return s

    def __footer(self) -> str:
        """Prints a footer."""
        return "".center(self._terminal_width, '=') + '\n'

    def _display_content(self, title: str, body: str, margin: int = 6):
        """Prints the body."""
        header = self.__header(title)
        print(header)
        print(body)
        footer = self.__footer()
        print(footer)

        header_lines = len(header.splitlines())
        body_lines = len(body.splitlines())
        footer_lines = len(footer.splitlines())
        content_lines = header_lines + body_lines + footer_lines + margin
        span = int(self._terminal_height - content_lines)
        print('\n' * span)

    def _flush_session_message(self):
        """Flushes the message when present."""
        if self._base.success:
            session(f"[bold green]{self._base.message}[/bold green]")
        else:
            session(f"[bold red]{self._base.message}[/bold red]")

        self._base.message = ''
        self._base.success = True

    def _refresh_display(self, title: str, body: str):
        """Refreshes display upon a cycle of a process."""
        self._clear_screen()
        self._display_content(title, body)
        self._flush_session_message()

    def _append_error_message(self, message: str):
        """Adds an error message to the session."""
        self._base.message = message
        self._base.success = False

    def _append_success_message(self, message: str):
        """Adds a success message to the session."""
        self._base.message = message
        self._base.success = True

    def _option_entry_handler(self) -> int | None:
        """Handles the option number input by the user."""
        entry = input("Enter option number: ").strip()
        self._loading()

        if len(entry) == 0:
            return None

        if entry.isnumeric():
            return int(entry)

        return -1

    def __spinner(self):
        """Provides a spinner animation in the terminal."""
        symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
        i = 0

        while self._base.animated:
            i = (i + 1) % len(symbols)
            stdout.write(f'\r\033[K{symbols[i]} ')
            stdout.flush()
            time.sleep(.05)

    def _loading(self):
        """Buffers the process to simulate the loading animation."""
        self._base.animated = True

        loading_thread = threading.Thread(target=self.__spinner)
        loading_thread.daemon = True
        loading_thread.start()
        time.sleep(.5)

        self._base.animated = False

    def _reset_external_contexts(self):
        """Resets external contexts to default after a process of subprogram is done."""
        self._extrn.resume = True
        self._extrn.valid = False
        self._reset_edge_contexts()

    def _reset_edge_contexts(self):
        """Resets edge contexts to default after a process of defining weight."""
        self._edg.two_direction = False
        self._edg.weight = False
        self._edg.int_weight = False
        self._edg.first_weight = False
        self._edg.second_weight = False
        self._edg.weight_list = []

    def _reset_graph_contexts(self):
        """Resets MST contexts to default after running algorithms."""
        self._grph.run = False
