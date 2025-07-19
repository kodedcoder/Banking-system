class Admin:
    def __init__(self, fname, lname, address, username, password, super_user):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.username = username
        self.password = password
        self.super_user = super_user

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_first_name(self):
        return self.fname

    def get_last_name(self):
        return self.lname
