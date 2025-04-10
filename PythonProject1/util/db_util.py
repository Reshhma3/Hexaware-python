

import pyodbc

class DatabaseConnector:
    def __init__(self):
        self.conn = None

    def open_connection(self):
        self.conn = pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=RESHHMA-VIVOBOO;"
            "DATABASE=TechShopDB;"
            "Trusted_Connection=yes;"
        )
        return self.conn

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def get_cursor(self):
        if not self.conn:
            self.open_connection()
        return self.conn.cursor()