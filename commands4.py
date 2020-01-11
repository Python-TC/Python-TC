def create_folder(self, path):
        """Create folder of the path"""
        if self.is_logged_in:
            current_abs_dir = join("file_data", self.username, self.current_directory)
            already_available_directories = []
            for sub in os.listdir(current_abs_dir):
                if isdir(join(current_abs_dir, sub)):
                    already_available_directories.append(sub)
            if path in already_available_directories:
                return "\nDirectory Already Present"
            os.mkdir(join(current_abs_dir, path))
            return "\nSuccessfully made directory"
        return "\nYou need to login to execute this command."

    def execute(self, statement):
        """Worker execute"""
        # Todo use switch for better
        statement = statement.rstrip("\n")
        com = statement.split(" ")[0]
        if com == "commands":
            return self.commands()
        if com == "register":
            if len(statement.split(" ")) == 4:
                return self.register(statement.split(" ")[1], statement.split(" ")[2], statement.split(" ")[3])
            return "Make sure you have typed correct command"
        if com == "quit":
            return self.quit()
        if com == "login":
            if len(statement.split(" ")) == 3:
                return self.login(statement.split(" ")[1], statement.split(" ")[2])
            return "Make sure you have typed correct command"
        if com == "list":
            return self.list()
        if com == "change_folder":
            return self.change_folder(statement.split(" ")[1])
        if com == "read_file":
            return self.read_file(statement.split(" ")[1])
        if com == "write_file":
            return self.write_file(statement.split(" ")[1], " ".join(statement.split(" ")[2:]))
        if com == "create_folder":
            return self.create_folder(statement.split(" ")[1])
        if com == "delete":
            return self.delete(statement.split(" ")[1], statement.split(" ")[2])
        return "Invalid command"