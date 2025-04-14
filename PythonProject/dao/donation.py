'''from util.db import DBConnUtil

class DonationDAO:
    @staticmethod
    def add_donation(donor_name, amount):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO donations (donor_name, amount, donation_date) VALUES (?, ?, GETDATE())",
                (donor_name, amount)
            )
            conn.commit()
            conn.close()
        except Exception as e:
            print("Error adding donation:", e)'''

'''from util.db import DBConnUtil
from datetime import datetime

class DonationDAO:
    @staticmethod
    def add_donation(donor_name, donation_type, donation_amount, donation_item):
        db = DBConnUtil()
        conn = db.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO Donations (DonorName, DonationType, DonationAmount, DonationItem, DonationDate)
                VALUES (?, ?, ?, ?, ?)
            """, (donor_name, donation_type, float(donation_amount), donation_item, datetime.now().date()))
            conn.commit()
            print("✅ Donation added successfully!")
        except Exception as e:
            print("❌ Error adding donation:", e)
        finally:
            db.get_connection()'''

from util.db import DBConnUtil
import datetime

class DonationDAO:
    @staticmethod
    def add_donation(donor_name, donation_type, donation_amount, donation_item):
        try:
            db = DBConnUtil()
            conn = db.get_connection()
            cursor = conn.cursor()

            # Safely convert and clean all parameters
            donor_name = str(donor_name) if donor_name else ""
            donation_type = str(donation_type) if donation_type else ""
            donation_item = str(donation_item) if donation_item else ""
            donation_amount = float(donation_amount) if donation_amount else 0.0
            donation_date = datetime.datetime.now().strftime('%Y-%m-%d')  # Format date as string

            # SQL Insert
            cursor.execute("""
                INSERT INTO Donations (DonorName, DonationType, DonationAmount, DonationItem, DonationDate)
                VALUES (?, ?, ?, ?, ?)
            """, (donor_name, donation_type, donation_amount, donation_item, donation_date))

            conn.commit()
            print("✅ Donation added successfully!")

        except Exception as e:
            print("❌ Error adding donation:", e)

        finally:
            if conn:
                conn.close()



