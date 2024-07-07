
class Customer:
    def __init__(self, customer_id, name, membership=False):
        self.customer_id = customer_id
        self.name = name
        self.membership = membership

    def apply_membership(self):
        self.membership = True

    def remove_membership(self):
        self.membership = False
