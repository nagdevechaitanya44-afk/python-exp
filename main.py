import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


print("==============================================")
print("        ADDRESS BOOK MANAGEMENT SYSTEM")
print("==============================================")

print("1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Update Contact")
print("5. Delete Contact")
print("6. Exit")

print("==============================================")

choice = input("Enter your choice: ")


if choice == "1":

    print("\n----------- ADD CONTACT -----------")

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    address = input("Enter Postal Address: ")
    contact_type = input("Enter Contact Type (Personal/Work): ")
    company = input("Enter Company Name: ")
    notes = input("Enter Notes: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "contact_type": contact_type,
        "company": company,
        "notes": notes
    }

    contacts = load_contacts()

    contacts.append(contact)

    save_contacts(contacts)

    print("\nContact added successfully!")


elif choice == "2":

    print("\nView Contacts selected")


elif choice == "3":

    print("\nSearch Contact selected")


elif choice == "4":

    print("\nUpdate Contact selected")


elif choice == "5":

    print("\nDelete Contact selected")


elif choice == "6":

    print("\nThank you for using Address Book!")


else:

    print("\nInvalid choice! Please enter a number from 1 to 6.")