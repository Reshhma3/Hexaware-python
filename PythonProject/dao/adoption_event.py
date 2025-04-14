'''from util.db import DBConnUtil

class AdoptionEventDAO:
    @staticmethod
    def get_events():
        events = []
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT event_id, event_name, event_date FROM adoption_events")
            events = cursor.fetchall()
            cursor.execute("SELECT event_id, event_name, event_date FROM adoption_events")

            conn.close()
        except Exception as e:
            print("Error retrieving events:", e)
        return events

    @staticmethod
    def add_participant(EventId, ParticipantName):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO participants (EventId, ParticipantName) VALUES (?, ?)",
                           (EventId, ParticipantName))
            conn.commit()
            conn.close()
        except Exception as e:
            print("Error adding participant:",e)'''

from util.db import DBConnUtil

''''@staticmethod
def get_events():
    try:
        db = DBConnUtil()
        conn = db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM AdoptionEvents")
        events = cursor.fetchall()
        return events  # ✅ Add this!

    except Exception as e:
        print("Error retrieving events:", e)
        return []  # ✅ Safe fallback to avoid NoneType error

    finally:
        if conn:
            conn.close()'''

'''from util.db import DBConnUtil

class AdoptionEventDAO:
    @staticmethod
    def add_participant(event_id, participant_name, participant_type):
        try:
            db = DBConnUtil()
            conn = db.get_connection()
            cursor = conn.cursor()

            # 👇 Do NOT include ParticipantID — it's auto-generated
            cursor.execute("""
                INSERT INTO Participants (ParticipantName, ParticipantType, EventID)
                VALUES (?, ?, ?)
            """, (participant_name, participant_type, event_id))

            conn.commit()
            print("✅ Participant registered successfully!")

        except Exception as e:
            print("❌ Error adding participant:", e)

        finally:
            if conn:
                conn.close()'''

import pyodbc
from util.db import DBConnUtil  # assuming you have a config file for DB connection

import random

unique_id = random.randint(1000, 9999)  # Ideally query max ID +
conn = DBConnUtil.get_connection()


class AdoptionEventDAO:
    @staticmethod
    def add_participant(event_id, name, participant_type):
        conn = None
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Participants (ParticipantID, EventID, ParticipantName, ParticipantType)
                VALUES (?, ?, ?, ?)
            """, (unique_id, event_id, name, participant_type))

            conn.commit()
            print("✅ Participant registered successfully!")
        except Exception as e:
            print("❌ Error adding participant:", e)
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_events():
        conn = None
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT EventID, EventName, EventDate FROM AdoptionEvents")
            return cursor.fetchall()
        except Exception as e:
            print("❌ Error fetching events:", e)
            return []
        finally:
            if conn:
                conn.close()






