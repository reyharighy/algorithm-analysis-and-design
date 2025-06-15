"""A module to provide shared funtionality accross all programs"""

import os
import time
import threading
from sys import stdout
from rich import print as session

class BaseProgram:
    """A class to provide basic operation when using a program."""

    def __init__(self) -> None:
        self._terminate: bool = False
        self._animated: bool = False
        self._session_message: str = ''
        self._success_message: bool = True
        self._terminal_height: int = int(os.popen('stty size', 'r').read().split()[0])
        self._terminal_width: int = int(os.popen('stty size', 'r').read().split()[1])

    def start(self):
        """Not implemented."""

    def save_exit(self):
        """Not implemented."""

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
        span = int(self._terminal_height - header_lines - body_lines - footer_lines - margin)
        print('\n' * span)

    def _flush_session_message(self):
        """Flushes the message when present."""
        if self._success_message:
            session(f"[bold green]{self._session_message}[/bold green]")
        else:
            session(f"[bold red]{self._session_message}[/bold red]")

        self._session_message = ''
        self._success_message = True

    def _append_error_message(self, message: str):
        """Adds an error message to the session."""
        self._session_message = message
        self._success_message = False

    def _append_success_message(self, message: str):
        """Adds a success message to the session."""
        self._session_message = message
        self._success_message = True

    def _option_entry_handler(self) -> int | None:
        """Handles the option number input by the user."""
        entry = input("Enter option number: ").strip()

        if len(entry) == 0:
            return None

        if entry.isnumeric():
            return int(entry)

        return -1

    def __spinner(self):
        """Provides a spinner animation in the terminal."""
        symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
        i = 0

        while self._animated:
            i = (i + 1) % len(symbols)
            stdout.write(f'\r\033[K{symbols[i]} ')
            stdout.flush()
            time.sleep(0.1)

    def _loading(self):
        """Buffers the process to simulate the loading animation."""
        self._animated = True

        loading_thread = threading.Thread(target=self.__spinner)
        loading_thread.daemon = True
        loading_thread.start()
        time.sleep(.5)

        self._animated = False
