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
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

def curly_braces_split(e_arg):
    """
    Splits the curly braces for the update method
    """
    curly_braces = re.search(r"\{(.*?)\}", e_arg)

    if curly_braces:
        id_with_comma = shlex.split(e_arg[:curly_braces.span()[0]])
        id = [i.strip(",") for i in id_with_comma][0]

        str_data = curly_braces.group(1)
        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return
        return id, arg_dict
    else:
        commands = e_arg.split(",")
        if commands:
            try:
                id = commands[0]
            except Exception:
                return "", ""
            try:
                attr_name = commands[1]
            except Exception:
                return id, ""
            try:
                attr_value = commands[2]
            except Exception:
                return id, attr_name
            return f"{id}", f"{attr_name} {attr_value}"

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "
    __classes_valid = ["BaseModel","User","Amenity",
                            "Place","Review","State","City"]

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

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid
        overrided.
        """
        # User.all() => ['User, 'all()']
        arg_list = arg.split('.')
        # incoming class name => User
        class_nm = arg_list[0]
        # all() => ['all', ') xxxxx']
        cmnd = arg_list[1].split('(')
        # incoming command method => all
        cmd_method = cmnd[0]
        # show User id => id extra arg
        e_arg = cmnd[1].split(')')[0]  # extra arguments
        method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if cmd_method in method_dict.keys():
            if cmd_method != "update":
                return method_dict[cmd_method]("{} {}".format(class_nm, e_arg))
            else:
                if not class_nm:
                    print("** class name missing **")
                    return
                try:
                    obj_id, arg_dict = curly_braces_split(e_arg)
                except Exception:
                    pass
                try:
                    call = method_dict[cmd_method]
                    return call("{} {} {}".format(class_nm, obj_id, arg_dict))
                except Exception:
                    pass
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False
    def do_count(self, arg):
        """
        Retrieve the number of instances of a class:
        <class name>.count()
        """
        objs = storage.all()
        cmnds = shlex.split(arg)
        if arg:
            class_nm = cmnds[0]
        count = 0
        if cmnds:
            if class_nm in HBNBCommand.__classes_valid:
                for obj in objs.values():
                    if obj.__class__.__name__ == class_nm:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()