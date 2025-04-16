import pyodbc

class DBConnUtil:

    @staticmethod
    def get_connection():
        try:
            # Hardcoded connection string
            connection_string = (
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=RESHHMA-VIVOBOO;"  
                "DATABASE=projectcasestudy;"        
                "Trusted_Connection=yes;"
            )

            # Connect to the database using the connection string
            conn = pyodbc.connect(connection_string)
            return conn
        except Exception as e:
            print(f"Error connecting to DB: {e}")
            return None

    @staticmethod
    def test_connection():
        # Test the connection and print result
        conn = DBConnUtil.get_connection()
        if conn:
            print("Database connection successful!")
            conn.close()
        else:
            print("Failed to connect to the database.")

# Example usage
if __name__ == "__main__":
    DBConnUtil.test_connection()
