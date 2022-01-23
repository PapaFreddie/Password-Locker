class User:


    user_list = []
    

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        pass


    def save_user(self):

        User.user_list.append(self)