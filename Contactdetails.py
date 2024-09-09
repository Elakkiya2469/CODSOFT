import sys

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email (optional): ")
    address = input("Enter address (optional): ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")

def view_contact_list():
    print("Contact List:")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}\n") 


def search_contact():
    query = input("Enter name or phone number to search: ")
    if query in contacts:
        print("Contact found:")
        print(contacts[query])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name of contact to update: ")
    if name in contacts:
        print("Enter new details:")
        phone = input("Enter new phone number (or leave blank to keep existing): ")
        email = input("Enter new email (or leave blank to keep existing): ")
        address = input("Enter new address (or leave blank to keep existing): ")
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address 

        print("Contact updated successfully!")
    else:
        print("Contact not found.") 


def delete_contact():
    name = input("Enter name of contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def save_contacts():
    with open("contacts.txt", "w") as f:
        for name, details in contacts.items():
            f.write(f"{name},{details['phone']},{details['email']},{details['address']}\n")
    print("Contacts saved successfully!")

def load_contacts():
    global contacts
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone, email, address = line.strip().split(",")
                contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contacts loaded successfully!")
    except FileNotFoundError:
        print("No contacts found.")

contacts = {}
load_contacts()

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")

    print("6. Save Contacts")
    print("7. Exit")
    choice = input("Enter your choice: ")

    try:
        choice = int(choice)
        if 1 <= choice <= 7:
            if choice == 1:
                add_contact()
            elif choice == 2:
                view_contact_list()
            elif choice == 3:
                search_contact()
            elif choice == 4:
                update_contact()
            elif choice == 5:
                delete_contact()
            elif choice == 6:
                save_contacts()
            elif choice == 7:
                print("Exiting...")
                sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 7: ")
    except ValueError:
        print("Invalid choice. Please enter a number (1-7): ")
