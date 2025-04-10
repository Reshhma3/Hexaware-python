from util.db_util import DatabaseConnector
from entity.customer import Customer

class CustomerDAO:
    @staticmethod
    def register_customer(customer):
        db = DatabaseConnector()
        conn = db.open_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
            VALUES (?, ?, ?, ?, ?)
        """, (customer.first_name, customer.last_name, customer.email, customer.phone, customer.address))
        conn.commit()
        db.close_connection()

