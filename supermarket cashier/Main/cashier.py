
class Cashier:
    def __init__(self, cashier_id, name):
        self.cashier_id = cashier_id
        self.name = name

    def process_payment(self, cart, payment_method):
        total = cart.calculate_total()
        payment_method.process(total)
        return cart.generate_receipt()
