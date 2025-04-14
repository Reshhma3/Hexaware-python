import pyodbc


class DBPropertyUtil:
    @staticmethod
    def get_connection_string():
        return (
            "DRIVER={SQL Server};"
            "SERVER=RESHHMA-VIVOBOO;"  
            "DATABASE=PetPals1;"       
            "Trusted_Connection=yes;"
        )

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            return pyodbc.connect(DBPropertyUtil.get_connection_string())
        except pyodbc.Error as e:
            print("Database connection error:", e)
            raise


