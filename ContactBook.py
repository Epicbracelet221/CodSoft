class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, contact_index, new_contact):
        if 1 <= contact_index <= len(self.contacts):
            self.contacts[contact_index - 1] = new_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, contact_index):
        if 1 <= contact_index <= len(self.contacts):
            del self.contacts[contact_index - 1]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")

def main():
    contact_book = ContactBook()
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)
        elif choice == '2':
            contact_book.view_contact_list()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_results = contact_book.search_contact(search_term)
            if search_results:
                print("Search Results:")
                for idx, contact in enumerate(search_results, start=1):
                    print(f"{idx}. {contact.name} - {contact.phone}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            contact_index = int(input("Enter contact index to update: "))
            if 1 <= contact_index <= len(contact_book.contacts):
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                updated_contact = Contact(name, phone, email, address)
                contact_book.update_contact(contact_index, updated_contact)
            else:
                print("Invalid contact index.")
        elif choice == '5':
            contact_index = int(input("Enter contact index to delete: "))
            contact_book.delete_contact(contact_index)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
