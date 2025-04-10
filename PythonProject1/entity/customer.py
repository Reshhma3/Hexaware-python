class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.orders = []

    def calculate_total_orders(self):
        return len(self.orders)

    def get_customer_details(self):
        return f"{self.__first_name} {self.__last_name}, {self.__email}, {self.__phone}, {self.__address}"

    def update_customer_info(self, email=None, phone=None, address=None):
        if email: self.__email = email
        if phone: self.__phone = phone
        if address: self.__address = address

    @property
    def customer_id(self): return self.__customer_id
    @property
    def first_name(self): return self.__first_name
    @property
    def last_name(self): return self.__last_name
    @property
    def email(self): return self.__email
    @property
    def phone(self): return self.__phone
    @property
    def address(self): return self.__address