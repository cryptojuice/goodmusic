import unittest
from pymongo import MongoClient
from app import app


class UsersTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.client = MongoClient('192.168.33.13', 27017)
        self.db = self.client.testdb
        self.collection = self.db.users

    def tearDown(self):
        self.db.drop_collection('users')


    # helper functions

    def register(self, username, password, password2=None, email=None):
        if password2 is None:
            password2 = password
        if email is None:
            email = username + '@example.com'
        return self.app.post('/users/register', data={
            'username': username,
            'password': password,
            'password2': password2,
            'email': email,
            }, follow_redirects=True)

    def login(self, username, password):
        pass

    # test functions

    def test_register(self):
        rv = self.register('user1', 'default')
        assert b'You where successfully registered' in rv.data

    def test_login(self):
        pass

if __name__ == "__main__":
    unittest.main()
