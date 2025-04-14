'''from dao.pet import PetDAO
from dao.donation import DonationDAO
from dao.adoption_event import AdoptionEventDAO

def menu():
    while True:
        print("\n--- PetPals Menu ---")
        print("1. View all pets")
        print("2. Add donation")
        print("3. View adoption events")
        print("4. Register for an event")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            pets = PetDAO.get_all_pets()
            for pet in pets:
                print(pet)

        elif choice == "2":


            donor_name = input("Donor Name: ")
            donation_type = input("Donation Type (Cash/Item): ")
            donation_amount = float(input("Amount: "))
            donation_item = input("Donation Item: ")

            DonationDAO.add_donation(donor_name, donation_type, donation_amount, donation_item)



        elif choice == "3":
            events = AdoptionEventDAO.get_events()
            for e in events:
                print(f"ID: {e[0]}, Name: {e[1]}, Date: {e[2]}")

        elif choice == "4":
            event_id = int(input("Enter Event ID: "))
            name = input("Participant Name: ")
            AdoptionEventDAO.add_participant(event_id, name)

        elif choice == "5":
            print("Exiting PetPals...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()'''

from dao.pet import PetDAO
from dao.donation import DonationDAO
from dao.adoption_event import AdoptionEventDAO

def menu():
    while True:
        print("\n--- 🐾 PetPals Menu 🐾---")
        print("1. View all pets🐶")
        print("2. Add donation💝")
        print("3. View adoption events📅")
        print("4. Register for an event📝")
        print("5. Exit❌")

        choice = input("Enter choice: ")

        if choice == "1":
            pets = PetDAO.get_all_pets()
            for pet in pets:
                print(pet)

        elif choice == "2":
            donor_name = input("Donor Name: ")
            donation_type = input("Donation Type (Cash/Item): ")
            donation_amount = float(input("Amount: "))
            donation_item = input("Donation Item: ")

            DonationDAO.add_donation(donor_name, donation_type, donation_amount, donation_item)

        elif choice == "3":
            events = AdoptionEventDAO.get_events()
            for e in events:
                print(f"ID: {e[0]}, Name: {e[1]}, Date: {e[2]}")

        elif choice == "4":
            event_id = int(input("Enter Event ID: "))
            name = input("Participant Name: ")
            participant_type = input("Participant Type (Adopter/Volunteer): ")


            AdoptionEventDAO.add_participant(event_id, name,participant_type)

        elif choice == "5":
            print("Exiting PetPals👋👋...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()





