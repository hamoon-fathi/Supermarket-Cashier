
class Membership:
    def __init__(self):
        self.members = []

    def add_member(self, customer):
        if customer not in self.members:
            self.members.append(customer)
            customer.apply_membership()

    def remove_member(self, customer):
        if customer in self.members:
            self.members.remove(customer)
            customer.remove_membership()
