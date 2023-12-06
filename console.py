#!/usr/bin/python3
"""
Module for console
the entry point of the command interpreter
"""
import cmd
import shlex
import re
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "
    __classes_valid = {
        "BaseModel",
        "User",
        
    }

    def emptyline(self) -> bool:
        """ Do nothing when emty line entered """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True
    
    def do_EOF(self, arg):
        """
        EOF or Ctrl+D signal to exit the program.
        """
        return True
    
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """
        cmnds = shlex.split(arg)

        if len(cmnds) == 0:
            print("** class name missing **")
        elif cmnds[0] not in HBNBCommand.__classes_valid:
            print("** class doesn't exist **")
        else:
            nw_instance = eval(f"{cmnds[0]}()")
            storage.save()
            print(nw_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance 
        based on the class name and id.
        """
        cmnds = shlex.split(arg)

        if len(cmnds) == 0:
            print("** class name missing **")
        elif cmnds[0] not in HBNBCommand.__classes_valid:
            print("** class doesn't exist **")
        elif len(cmnds) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(cmnds[0], cmnds[1])
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and 
        id (save the change into the JSON file).
        """
        cmnds = shlex.split(arg)

        if len(cmnds) == 0:
            print("** class name missing **")
        elif cmnds[0] not in HBNBCommand.__classes_valid:
            print("** class doesn't exist **")
        elif len(cmnds) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(cmnds[0], cmnds[1])
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all 
        instances based or not on the class name.
        """
        objs = storage.all()
        cmnds = shlex.split(arg)
        if len(cmnds) == 0:
            for k, v in objs.items():
                print(str(v))
        elif cmnds[0] not in HBNBCommand.__classes_valid:
            print("** class doesn't exist **")
        else:
            for k, v in objs.items():
                if k.split('.')[0] == cmnds[0]:
                    print(str(v))
    
    def do_update(self, arg):
        """
        Updates an instance based on the class name 
        and id by adding or updating attribute 
        (save the change into the JSON file). 
        Update "<attribute_value>"
        """
        cmnds = shlex.split(arg)
        if len(cmnds) == 0:
            print("** class name missing **")
        elif cmnds[0] not in HBNBCommand.__classes_valid:
            print("** class doesn't exist **")
        elif len(cmnds) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(cmnds[0], cmnds[1])
            if key not in objects:
                print("** no instance found **")
            elif len(cmnds) < 3:
                print("** attribute name missing **")
            elif len(cmnds) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = cmnds[2]
                attr_value = cmnds[3]
                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()