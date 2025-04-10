class Inventory:
    def __init__(self):
        self.stock = {}

    def add_product(self, product, quantity):
        if product.product_id in self.stock:
            raise Exception("Duplicate product.")
        self.stock[product.product_id] = {"product": product, "quantity": quantity}

    def add_to_inventory(self, product_id, quantity):
        if product_id in self.stock:
            self.stock[product_id]["quantity"] += quantity

    def remove_from_inventory(self, product_id, quantity):
        if self.stock[product_id]["quantity"] < quantity:
            raise Exception("Insufficient stock.")
        self.stock[product_id]["quantity"] -= quantity

    def get_quantity_in_stock(self, product_id):
        return self.stock.get(product_id, {}).get("quantity", 0)

    def is_product_available(self, product_id, qty):
        return self.get_quantity_in_stock(product_id) >= qty

    def get_inventory_value(self):
        return sum(p["product"].price * p["quantity"] for p in self.stock.values())

    def list_low_stock_products(self, threshold):
        return [(p["product"].name, p["quantity"]) for p in self.stock.values() if p["quantity"] < threshold]

    def list_out_of_stock_products(self):
        return [p["product"].name for p in self.stock.values() if p["quantity"] == 0]

    def list_all_products(self):
        return [(p["product"].name, p["quantity"]) for p in self.stock.values()]