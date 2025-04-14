
import pyodbc
from util.db import DBConnUtil
from entity.pet import Pet

class PetDAO:
    @staticmethod
    def get_all_pets():
        pets = []
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT name, age, breed FROM pets")
            for row in cursor.fetchall():
                pets.append(Pet(row[0], row[1], row[2]))
            conn.close()
        except Exception as e:
            print("Error fetching pets:", e)
        return pets
