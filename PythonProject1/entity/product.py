class Product:
    def __init__(self, product_id, name, description, price):
        self.__product_id = product_id
        self.__name = name
        self.__description = description
        self.__price = price

    def get_product_details(self):
        return f"{self.__name} - {self.__description} - ₹{self.__price}"

    def update_product_info(self, price=None, description=None):
        if price is not None:
            if price < 0:
                raise ValueError("Price must be non-negative.")
            self.__price = price
        if description:
            self.__description = description

    @property
    def price(self): return self.__price
    @property
    def name(self): return self.__name
    @property
    def product_id(self): return self.__product_id
    @property
    def description(self): return self.__description
