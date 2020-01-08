import json
import os
import shutil
from os.path import join, normpath, realpath, isfile, isdir

class Worker():
    """
    Class - Worker
    Manages all the user commands and its interactions
    """
    def __init__(self, ip):
        """Constructor of class"""
        self.ip = ip
        self.username = None
        self.is_logged_in = False
        self.login_credentials = None
        self.reset_credentials()
        self.current_directory = None
        self.readed = {}

    def reset_credentials(self):
        """reset the login credentials on to a variable"""
        with open("credentials/credentials") as file:
            data = json.load(file)
        self.login_credentials = data

    def dump_credentials(self, file):
        """dump credentials to file"""
        try:
            with open("credentials/credentials", 'w') as outfile:
                json.dump(file, outfile)
        except:
            print("Error dumping data")

    def commands(self):
        """Print all available commands of server"""
        out = "\n"
        out += "-----------------------------------" + "\n"
        out += "--------    COMMANDS   ------------" + "\n"
        out += "-----------------------------------" + "\n"
        out += "Command" + "\n"
        out += "Description" + "\n"
        out += "----------------------" + "\n"
        out += "register <username> <password> <privileges>" + "\n"
        out += "Register a new user with the <username> <password> and <privileges> to the server." + "\n"
        out += "----------------------" + "\n"
        out += "login <username> <password>" + "\n"
        out += "Log in the user with <username> and <password>" + "\n"
        out += "----------------------" + "\n"
        out += "delete <username> <password>" + "\n"
        out += "Delete the user with <username> from the server. Can be executed only by admin." + "\n"
        out += "----------------------" + "\n"
        out += "change_folder <name>" + "\n"
        out += "Move the current directory to folder <name>" + "\n"
        out += "----------------------" + "\n"
        out += "list" + "\n"
        out += "Print all the files and folders in directory" + "\n"
        out += "----------------------" + "\n"
        out += "read_file <name>" + "\n"
        out += "Read 100 characters from the file <name> in the current directory" + "\n"
        out += "----------------------" + "\n"
        out += "write_file <name> <input>" + "\n"
        out += "Write data in <input> to end of file <name> in current directory" + "\n"
        out += "----------------------" + "\n"
        out += "create_folder <name>" + "\n"
        out += "Create a new folder with the <name> in the current directory" + "\n"
        out += "-----------------------------------" + "\n"
        out += "-----------------------------------" + "\n"
        out += "-----------------------------------" + "\n"
        return out
