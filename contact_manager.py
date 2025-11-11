# contact_manager.py

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"{name} added!")
    

def view_contacts(contacts):
    if not contacts:
        print("No contacts found")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

def search_contact(contacts):
    search_name = input("Enter name to search: ")
    found = [c for c in contacts if search_name.lower() in c['name'].lower()]
    if found:
        for contact in found:
            print(f"Found: {contact['name']} - {contact['phone']}")
    else:
        print("Not found")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    contacts[:] = [c for c in contacts if c['name'].lower() != name.lower()]
    print(f"{name} deleted!")

def save_contacts(contacts):
    with open("contacts.txt", "w") as f:
        for contact in contacts:
            f.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")
    print("Contacts saved!")

def load_contacts():
    contacts = []
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")
                contacts.append({"name": name, "phone": phone, "email": email})
    except FileNotFoundError:
        pass
    return contacts

def main():
    contacts = load_contacts()
    
    while True:
        print("\n=== CONTACT MANAGER ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ")
        
        if choice == "1":
           add_contact(contacts)
           print(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()