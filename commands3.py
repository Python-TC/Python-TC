import json
import os
import shutil
from os.path import join, normpath, realpath, isfile, isdir

class Worker():
    """
    Class - Worker
    Manages all the user commands and its interactions
    """
    def get_total_path(self, directory):
        """total path for the user"""
        total_path = join("file_data", self.username, self.current_directory, directory)
        real_path = realpath(total_path)
        return normpath(real_path)

    def change_folder(self, directory):
        """Change directory to specific folder"""
        if self.is_logged_in:
            total_dir = self.get_total_directories()
            path_to_be_change = self.get_total_path(directory)
            if path_to_be_change in total_dir:
                self.current_directory = join(self.current_directory, directory)
                return "\nChanged directory to " + directory + " successfully"
            return "\nWrong directory name."
        return "\nYou need to login to execute this command."

    def list(self):
        """List all the files and folders"""
        if self.is_logged_in:
            total_files = []
            for file in os.listdir(join("file_data", self.username, self.current_directory)):
                total_files.append(file)
            return "\n" + "\n".join(total_files)
        return "\nYou need to login to execute this command."

    def get_file_list(self):
        """list the files"""
        available_files = []
        for file in os.listdir(join("file_data", self.username, self.current_directory)):
            if isfile(join("file_data", self.username, self.current_directory, file)):
                available_files.append(file)
        return available_files

    def get_content(self, path):
        """get content from file"""
        char_at_a_time = 100
        abs_path = join("file_data", self.username, self.current_directory, path)
        if abs_path not in list(self.readed.keys()):
            self.readed[abs_path] = 0
        with open(abs_path, "r") as file:
            contents = file.read()
        content_from = str(self.readed[abs_path]*char_at_a_time)
        index = self.readed[abs_path]*char_at_a_time
        data = contents[index:(index+1)*char_at_a_time]
        self.readed[abs_path] += 1
        self.readed[abs_path] %= len(contents)//char_at_a_time + 1
        return "\n" + "Characters from " + content_from + " to " + str(int(content_from) + char_at_a_time) + " are - \n" + data

    def read_file(self, path):
        """Read file of the path"""
        if self.is_logged_in:
            total_files = self.get_file_list()
            if path in total_files:
                return self.get_content(path)
            return "\nUnable to open requested file. Check again."
        return "\nYou need to login to execute this command."

    def write_file(self, path, write_data):
        """Write file of the path"""
        write_data = "\n" + write_data
        abs_path = join("file_data", self.username, self.current_directory, path)
        if self.is_logged_in:
            total_files = self.get_file_list()
            if path in total_files:
                with open(abs_path, "a+") as file:
                    file.write(write_data)
                return "\nWritten successfully"
            with open(abs_path, "w+") as file:
                file.write(write_data)
            return "\nNo such file found\nWritten a new file\n"
        return "\nYou need to login to execute this command."