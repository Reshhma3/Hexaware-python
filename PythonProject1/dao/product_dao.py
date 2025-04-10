
from util.db_util import DatabaseConnector
from entity.product import Product

class ProductDAO:
    @staticmethod
    def add_product(product):
        db = DatabaseConnector()
        conn = db.open_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Products (ProductName, Description, Price)
            VALUES (?, ?, ?)
        """, (product.name, product.description, product.price))
        conn.commit()
        db.close_connection()

    @staticmethod
    def update_product_info(product):
        db = DatabaseConnector()
        conn = db.open_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Products SET Description = ?, Price = ? WHERE ProductID = ?
        """, (product.description, product.price, product.product_id))
        conn.commit()
        db.close_connection()

    @staticmethod
    def delete_product(product_id):
        db = DatabaseConnector()
        conn = db.open_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Products WHERE ProductID = ?", (product_id,))
        conn.commit()
        db.close_connection()

    @staticmethod
    def get_all_products():
        db = DatabaseConnector()
        conn = db.open_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ProductID, ProductName, Description, Price FROM Products")
        products = cursor.fetchall()
        db.close_connection()
        return products