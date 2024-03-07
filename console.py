#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command: exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command: exit the program"""
        print("Exiting...")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
