
from util.db_util import DatabaseConnector

class InventoryDAO:
    @staticmethod
    def reduce_stock(product_id, quantity):
        db = DatabaseConnector()
        conn = db.open_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Inventory
            SET QuantityInStock = QuantityInStock - ?
            WHERE ProductID = ? AND QuantityInStock >= ?
        """, (quantity, product_id, quantity))
        conn.commit()
        db.close_connection()