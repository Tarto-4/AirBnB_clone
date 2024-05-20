#!/usr/bin/python3
"""
Entry point for the HBNB command interpreter.
"""

from cmd import Cmd
from models import storage, BaseModel


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

    def do_show(self, inp):
        """
        Prints the string representation of an instance.
        """

        args = inp.split()

        if not args:
            print("** class name missing **")
            return

        try:
            class_name = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        obj = storage.all().get(f"{class_name}.{args[1]}")

        if not obj:
            print("** no instance found **")
            return

        print(obj)

    def do_destroy(self, inp):
        """
        Deletes an instance based on the class name and id.
        """

        args = inp.split()

        if not args:
            print("** class name missing **")
            return

        try:
            class_name = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        obj = storage.all().get(f"{class_name}.{args[1]}")

        if not obj:
            print("** no instance found **")
            return

        storage.delete(obj)
        storage.save()
        print(None)  # Following convention to not print anything

    def do_all(self, inp):
        """
        Prints all string representations of all instances.
        """

        args = inp.split()

        if args and args[0] != "all":
            print("** class doesn't exist **")
            return

        objects = storage.all().values()
        print([str(obj) for obj in objects])

    def do_update(self, inp):
        """
        Updates an instance based on the class name and id.
        """

        args = inp.split()

        if not args:
            print("** class name missing **")
            return

        try:
            class_name = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 4:
            if len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            return

        obj = storage.all().get(f"{class_name}.{args[1]}")

        if not obj:
            print("** no instance found **")
            return

        if args[2] in ("id", "created_at", "updated_at"):
            print("** cannot update reserved attributes **")
            return

        try:
