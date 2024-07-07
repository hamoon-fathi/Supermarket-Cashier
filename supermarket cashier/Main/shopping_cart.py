
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})

    def remove_product(self, product_id):
        self.items = [item for item in self.items if item['product'].product_id != product_id]

    def calculate_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.items)

    def generate_receipt(self):
        receipt = "\n".join([f"{item['product'].name}: {item['quantity']} x {item['product'].price}" for item in self.items])
        receipt += f"\nTotal: {self.calculate_total()}"
        return receipt
