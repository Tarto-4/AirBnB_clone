#!/usr/bin/python3
"""
Entry point for the HBNB command interpreter.
"""

from cmd import Cmd
from models import storage, BaseModel
from models.base_model import BaseModel
from models.storage import FileStorage


class CommandInterpreter:
    """Command interpreter for interacting with BaseModel objects."""

    storage = FileStorage()

    def __init__(self):
        """Initializes the command interpreter."""
        pass

    def execute(self, cmd_args):
        """Executes a command based on the provided arguments.

        Args:
            cmd_args (list): A list of arguments representing the command and its options.
        """

        if not cmd_args:
            return

        command, *args = cmd_args
        if command == "create":
            self.do_create(args)
        elif command == "show":
            self.do_show(args)
        elif command == "destroy":
            self.do_destroy(args)
        elif command == "all":
            self.do_all(args)
        elif command == "update":
            self.do_update(args)
        else:
            print("** Invalid command **")

    def do_create(self, args):
        """Creates a new instance of a BaseModel and saves it."""

        if not args:
            print("** class name missing **")
            return

        try:
            obj = eval(f"{args[0]}()")
        except NameError:
            print("** class doesn't exist **")
            return

        self.storage.new(obj)
        self.storage.save()
        print(obj.id)

    def do_show(self, args):
        """Shows the string representation of an instance based on class name and id."""

        if not args:
            print("** class name missing **")
            return

        try:
            class_name, *id_args = args
            obj = self.storage.all().get(f"{class_name}.{id_args[0]}")
        except NameError:
            print("** class doesn't exist **")
            return

        if not obj:
            print("** no instance found **")
            return

        print(obj)

    def do_destroy(self, args):
        """Deletes an instance based on class name and id."""

        if not args:
            print("** class name missing **")
            return

        try:
            class_name, *id_args = args
            obj = self.storage.all().get(f"{class_name}.{id_args[0]}")
        except NameError:
            print("** class doesn't exist **")
            return

        if not obj:
            print("** no instance found **")
            return

        self.storage.objects.pop(f"{class_name}.{id_args[0]}")
        self.storage.save()
        print(None)

    def do_all(self, args):
        """Prints all string representations of all instances, optionally filtered by class name."""

        objects = self.storage.all().values()
        if args and args[0]:
            try:
                class_name = args[0]
                objects = [obj for obj in objects if isinstance(obj, eval(class_name))]
            except NameError:
                print("** class doesn't exist **")
                return

        print([str(obj) for obj in objects])

    def do_update(self, args):
        """Updates an instance based on class name, id, attribute name, and value."""

        if len(args) < 4:
            print("** attribute name missing **" if len(args) == 3 else "** value missing **")
            return

        try:
            class_name, *id_args = args[:2]
            obj = self.storage.all().get(f"{class_name}.{id_args[0]}")
        except NameError:
            print("** class doesn't exist **")
            return

        if not obj:
            print("** no instance found **")
            return

        attr_name, value = args[2], args[3]

        if attr_name in ("id", "created_at", "updated_at"):
            print("** can't update attribute **")
            return

        try:
