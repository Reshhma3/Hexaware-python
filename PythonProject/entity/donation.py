from abc import ABC, abstractmethod

'''class Donation(ABC):
    def __init__(self, donor_name, amount):
        self.donor_name = donor_name
        self.amount = amount
        self.donation_date = donation_date

    @abstractmethod
    def record_donation(self):
        pass'''

from util.db import DBConnUtil
import datetime

class DonationDAO:
    @staticmethod
    def add_donation(donor_name, donation_type, donation_amount, donation_item):
        try:
            db = DBConnUtil()
            conn = db.get_connection()
            cursor = conn.cursor()

            # Ensure all fields are safe to pass
            donor_name = str(donor_name) if donor_name else ""
            donation_type = str(donation_type) if donation_type else ""
            donation_item = str(donation_item) if donation_item else ""
            donation_amount = float(donation_amount) if donation_amount else 0.0
            donation_date = datetime.datetime.now().strftime('%Y-%m-%d')  # Format date as string

            # Use a plain SQL string and format values to avoid bind issues
            sql = f"""
                INSERT INTO Donations (DonorName, DonationType, DonationAmount, DonationItem, DonationDate)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (donor_name, donation_type, donation_amount, donation_item, donation_date))

            conn.commit()
            print("✅ Donation added successfully!")

        except Exception as e:
            print("❌ Error adding donation:", e)

        finally:
            if conn:
                conn.close()

