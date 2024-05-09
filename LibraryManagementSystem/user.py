# user.py
from models import User

class UserManagement:
    def __init__(self):
        self.users = []

    def add_user(self, name, user_id):
        self.users.append(User(name, user_id))

    def list_users(self):
        for user in self.users:
            print(f"Name: {user.name}, User ID: {user.user_id}")
