class Order:
    def __init__(self, order_id, customer, order_date):
        self.__order_id = order_id
        self.__customer = customer
        self.__order_date = order_date
        self.__status = "Processing"
        self.order_details = []

    def calculate_total_amount(self):
        return sum(od.calculate_subtotal() for od in self.order_details)

    def get_order_details(self):
        return [(od.product.name, od.quantity) for od in self.order_details]

    def update_order_status(self, status):
        self.__status = status

    def cancel_order(self, inventory):
        for od in self.order_details:
            inventory.add_to_inventory(od.product.product_id, od.quantity)
        self.order_details.clear()
        self.__status = "Cancelled"