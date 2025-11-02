import os

# Text file that saves contacts

FILE_NAME = "contacts.txt"


# Check for file if exists

if os.path.exists(FILE_NAME):
    with open(FILE_NAME,"r") as f:
        contacts = [line.strip().split(",") for line in f.readlines()]

else:
    contacts = []

# Utility function for save contact after adding or deleting a contact

def save_contacts():
    with open(FILE_NAME,"w") as f:
        for contact in contacts:
            f.write(",".join(contact) + "\n")

# Menu

def show_menu():
    print("\n=== CONTACT BOOK MENU ===")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter choice (1-5):")

# View all contacts

    if choice == "1":
        if not contacts:
            print("No contacts found!")
        else:
            print("\nYour Contacts:")
            print("-"*40)
            for i,contact in enumerate(contacts,1):
                name,phone,email=contact
                if email == "":
                    email = "Not Provided"
                print(f"{i}. Name: {name}, Phone: {phone}, Email: {email}")
            print("-"*40)


# Save a contact
          
    elif choice == "2":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()

        if name and phone:
            if len(phone)!=10 or not phone.isdigit():
                print("Phone number should have exactly 10 digits (numbers only).")
               
            else:
                contacts.append([name,phone,email])
                save_contacts()
                print("Contact added successfully!")
             
        else:
            print("Name and phone are required!")
            

# Search a contact
            
    elif choice == "3":
        search = input("Enter name or phone to search: ").strip().lower()
        found = False
        for name, phone, email in contacts:
            if search in name.lower() or search in phone:
                print(f"Found → Name: {name}, Phone: {phone}, Email: {email or 'Not Provided'}")
                found = True
        if not found:
            print("No matching contact found.")
            

# Delete a contact

    elif choice == "4":
        if not contacts:
            print("No contacts to delete.")
        else:
            print("\nContacts:")
            for i, contact in enumerate(contacts, 1):
                name, phone, email = contact
                print(f"{i}. {name} - {phone}")
            try:
                index = int(input("Enter contact number to delete: ")) - 1
                if 0 <= index < len(contacts):
                    removed = contacts.pop(index)
                    save_contacts()
                    print(f"Deleted contact: {removed[0]}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

# exiting the program
                
    elif choice == "5":
        print("Exiting... Goodbye!")
        break

# if user enter invalid choice other than menu
    else:
        print("Invalid choice. Please try again.")
                            
