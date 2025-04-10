from util.db_util import DatabaseConnector

class OrderDetailDAO:
    @staticmethod
    def get_order_details_by_order_id(order_id):
        db = DatabaseConnector()
        conn = db.open_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT od.OrderDetailID, p.ProductName, od.Quantity, od.Discount,
                   (p.Price * od.Quantity - od.Discount) AS Subtotal
            FROM OrderDetails od
            JOIN Products p ON od.ProductID = p.ProductID
            WHERE od.OrderID = ?
        """, (order_id,))
        results = cursor.fetchall()
        db.close_connection()
        return results