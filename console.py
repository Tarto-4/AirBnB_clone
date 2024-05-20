#!/usr/bin/python3
"""
Entry point for the HBNB command interpreter.
"""

from cmd import Cmd
from models import storage, BaseModel
import sys


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

    def emptyline(self, inp):
        """
        Handles empty lines by passing without execution.
        """
        pass

    def do_create(self, inp):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        """

        args = inp.split()

        if not args:
            print("** class name missing **")
            return

        try:
            new_obj = eval(args[0])()
        except NameError:
            print("** class doesn't exist **")
            return

        storage.new(new_obj)
        storage.save()
        print(new_obj.id)

    # ... other command definitions (do_show, do_destroy, etc.) ...

    def preloop(self):
        """
        Overridden preloop method to handle non-interactive input.
        """

        if not sys.stdin.isatty():  # Check if input is not coming from a terminal
            args = sys.stdin.read().strip().split("\n")
            for line in args:
                self.onecmd(line.strip())  # Process each line as a command

    def postloop(self):
        """
        Overridden postloop method to print a newline after non-interactive input.
        """

        if not sys.stdin.isatty():
            print("")  # Print a newline after processing non-interactive input

# ... main loop ...


if __name__ == "__main__":
    HBNBCommand().cmdloop()
