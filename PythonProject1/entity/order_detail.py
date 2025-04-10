class OrderDetail:
    def __init__(self, detail_id, order, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.detail_id = detail_id
        self.order = order
        self.product = product
        self.quantity = quantity
        self.discount = 0.0

    def calculate_subtotal(self):
        return (self.product.price * self.quantity) - self.discount

    def get_order_detail_info(self):
        return f"{self.product.name}: Qty {self.quantity}, Subtotal ₹{self.calculate_subtotal()}"

    def update_quantity(self, new_quantity):
        if new_quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.quantity = new_quantity

    def add_discount(self, discount):
        self.discount = discount