
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].update_quantity(quantity)

    def check_stock(self, product_id):
        return self.products.get(product_id, None).quantity if product_id in self.products else None
