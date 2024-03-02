#!/usr/bin/python3
"""console module"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quit command to exit console"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit console"""
        return True

    def emptyline(self):
        """doesn't execute anything"""
        pass

    def do_create(self, arg=None):
        """Create an instance of class"""
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            storage.save()

    def do_show(self, arg):
        """show instance based on class name and ID"""
        argl = arg.split()
        obj = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in globals():
            print("** class doesn't exist **")
        elif len(argl) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in obj:
            print("** no instance found **")
        else:
            print(obj["{}.{}".format(argl[0], argl[1])])


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        obj = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj:
            print("** no instance found **")
        else:
            del obj["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Display all instances based on class name"""
        args = arg.split()
        obj = storage.all()
        if len(args) > 0 and args[0] not in globals():
            print("** class doesn't exist **")
        else:
            print([str(obj[key]) for key in obj])

    def do_update(self, arg):
        """update an instance attribute"""
        arg = arg.split()
        obj = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in globals():
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj:
            print("** no instance found **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            instance = obj["{}.{}".format(arg[0], arg[1])]
            setattr(instance, arg[2], arg[3].strip('"'))
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
