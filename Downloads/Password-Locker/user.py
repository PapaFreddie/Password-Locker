class User:


    user_list = []
    

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def save_user(self):

        User.user_list.append(self)
