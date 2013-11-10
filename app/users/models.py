import datetime
from app import db

class User(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    email = db.EmailField(required=True)
    accounts = db.DictField()
    

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
    
