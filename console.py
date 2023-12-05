#!/usr/bin/python3
"""
Module for console
the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True
    
    def do_EOF(self, arg):
        """
        EOF or Ctrl+D signal to exit the program.
        """
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()