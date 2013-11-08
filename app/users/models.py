from app.config.database import db

collection = db.users

class User:

    def __init__(self, _id=None, email=None, username=None, password=None):
        self._id = _id
        self.email = email
        self.username = username
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
