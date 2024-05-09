# checkout.py
from models import Checkout

class CheckoutManagement:
    def __init__(self):
        self.checkouts = []

    def checkout_book(self, user_id, isbn):
        self.checkouts.append(Checkout(user_id, isbn))

    def list_checkouts(self):
        for checkout in self.checkouts:
            print(f"User ID: {checkout.user_id}, ISBN: {checkout.isbn}")
