from cgi import test
import unittest 

from user import User

class TestUser(unittest.TextCase):
    def tearDown(self):
        User.username = []
    
    def SetUp(self):
        self.new_username = User('Papa', '05121')
    

    def test_init(self):
        self.assertEqual(self.new_username, 'Papa')
        self.assertEqual(self.new_password, '05121')

    def test_save_user(self):
        self.new_username.save_user()
        self.assertEqual(len(User.username),1)

    def test_save_multiple_unsernames(self):
        
        self.new_username.save_username()
        test_username = User('abc', 'def', 'ghi', 'jkl')
        test
