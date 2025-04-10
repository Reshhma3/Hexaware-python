


from util.db_util import DatabaseConnector
from entity.order_detail import OrderDetail
from dao.inventory_dao import InventoryDAO
from datetime import datetime

class OrderDAO:
    @staticmethod
    def create_order(customer_id, order_date, total, order_details):
        db = DatabaseConnector()
        conn = db.open_connection()
        cursor = conn.cursor()

        # Ensure order_date is a string in 'YYYY-MM-DD' format
        if isinstance(order_date, datetime):
            order_date = order_date.strftime('%Y-%m-%d')
        elif not isinstance(order_date, str):
            order_date = str(order_date)

        # Check if customer exists
        cursor.execute("SELECT COUNT(*) FROM Customers WHERE CustomerID = ?", (customer_id,))
        if cursor.fetchone()[0] == 0:
            raise ValueError(f"Customer with ID {customer_id} does not exist. Please register the customer first.")

        # Check if all products exist before placing the order
        for detail in order_details:
            cursor.execute("SELECT COUNT(*) FROM Products WHERE ProductID = ?", (detail.product.product_id,))
            if cursor.fetchone()[0] == 0:
                raise ValueError(f"Product with ID {detail.product.product_id} does not exist. Please add the product first.")

        # Insert the order
        cursor.execute("""
            INSERT INTO Orders (CustomerID, OrderDate, TotalAmount)
            VALUES (?, ?, ?)
        """, (customer_id, order_date, total))

        # Get the inserted order ID
        cursor.execute("SELECT SCOPE_IDENTITY()")
        order_id = cursor.fetchone()[0]

        # Insert each order detail
        for detail in order_details:
            try:
                cursor.execute("""
                    INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Discount)
                    VALUES (?, ?, ?, ?)
                """, (order_id, detail.product.product_id, detail.quantity, detail.discount))

                # Update inventory
                InventoryDAO.reduce_stock(detail.product.product_id, detail.quantity)
            except Exception as e:
                print(f"Error inserting order detail for ProductID {detail.product.product_id}: {e}")

        conn.commit()
        db.close_connection()