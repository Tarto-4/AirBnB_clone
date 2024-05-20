#!/usr/bin/python3
"""
Entry point for the HBNB command interpreter.
"""

from cmd import Cmd


class HBNBCommand(Cmd):
    """
    HBNB command interpreter class.
    """

    prompt = "(hbnb) "
    intro = "Welcome to the HBNB command interpreter!"

    def do_quit(self, inp):
        """
        Quits the command interpreter.
        """
        print("Quitting HBNB, come back soon!")
        exit()

    def do_EOF(self, inp):
        """
        Quits the command interpreter (same as quit).
        """
        print("Quitting HBNB, come back soon!")
        exit()

    def emptyline(self):
        """
        Handles empty lines by passing without execution.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()