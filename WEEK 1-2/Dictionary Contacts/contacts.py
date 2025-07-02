# Empty Dictionary to store contacts

contacts = {}

# Function to add a contact
def add_contact(name, number):
    contacts[name] = number
    print(f" {name} added Successfully!")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        print(f" {name}: {contacts[name]}")
    else:
        print (f" No contact found for '{name}'.")

# Function to show all contacts
def show_all_contacts():
    if not contacts:
        print("No contacts saved yet.")
    else:
        print("Your Contacts:")
        for name, number in contacts.items():
            print(f"- {name}: {number}")

# Main Loop
while True:
    print("\n Contact Book Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Show All Contacts")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        add_contact(name, number)
        
    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)
        
    elif choice == "3":
        show_all_contacts()
        
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose 1–4.")



