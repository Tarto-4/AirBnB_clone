#!/usr/bin/python3
"""Entry point for the AirBnB command interpreter."""

from cmd import Cmd

class HBNBCommand(Cmd):
    """
    Command interpreter class for the AirBnB clone.
    """

    prompt = "(hbnb) "
    intro = "Welcome to the AirBnB command interpreter!"

    def do_quit(self, arg):
        """Quit command to exit the program.

        Args:
            arg (str, optional): Optional argument (ignored).
        """

        print("Bye!")
        exit(0)

    def emptyline(self):
        """Handle empty lines by passing (without any action)."""

        pass

    def do_EOF(self, arg):
        """EOF command to exit the program (same as quit).

        Args:
            arg (str, optional): Optional argument (ignored).
        """

        print("Bye!")
        exit(0)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
