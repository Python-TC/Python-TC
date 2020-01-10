def set_login(self, user):
        """set login confirmed"""
        self.is_logged_in = True
        self.username = user
        self.current_directory = ""

    def get_password(self, user):
        """Get password for username"""
        user_data = self.login_credentials[user]
        return user_data[0]

    def login(self, user, password):
        """login function"""
        if not self.is_logged_in:
            if user in list(self.login_credentials.keys()):
                if password == self.get_password(user):
                    self.set_login(user)
                    return "\nLogin completed."
                return "\nWrong password!"
            return "\nUsername not registered"
        return "\nYou have logged in already."

    def quit(self):
        """quit function"""
        try:
            self.current_directory = ""
            self.is_logged_in = False
            self.username = None
            self.read_file_status = {}
            return "\nLogged out"
        except KeyError:
            return "\nLogged out"

    def register(self, user, password, privileges):
        """Register function"""
        if user in list(self.login_credentials.keys()):
            return "\nUsername not available. Choose a new username."
        if user == "" or password == "" or privileges == "":
            return "\nYou cannot register empty user"
        users = self.login_credentials
        users[user] = [password, privileges]
        self.dump_credentials(users)
        self.reset_credentials()
        os.mkdir(join("file_data", user))
        return "\nRegistered user successfully. Now you can login."

    def remove_user_data(self, user):
        """remove the user's data"""
        user_path = join("file_data", user)
        shutil.rmtree(user_path)

    def delete(self, user, password):
        """Delete function"""
        if self.is_logged_in:
            if self.login_credentials[self.username][1] == "admin":
                if user in list(self.login_credentials.keys()):
                    if password == self.get_password(self.username):
                        del self.login_credentials[user]
                        self.dump_credentials(self.login_credentials)
                        if user == self.username:
                            self.is_logged_in = False
                        self.remove_user_data(user)
                        return "\nDeleted user with username " + user + " successfully"
                    return "\nYou have entered wrong password"
                return "\nNo such user with username " + user + " found"
            return "\nYou don't have privileges of an admin!"
        return "\nYou need to login to execute this command."

    def get_total_directories(self):
        """get total directies for the user"""
        total = []
        for direc, files, sub in os.walk(join("file_data", self.username)):
            total.append(normpath(realpath(direc)))
        return total
