# using functions
def add_contact(address_book):
    """
    Adds a new contact to the address book.
    Takes user input for contact details and stores them in the address_book list.
    """
    try:
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip_code = input("Enter Zip: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contact = [first_name, last_name, address, city, state, zip_code, phone, email]
        address_book.append(contact)
        print("Contact added successfully!")
    
    except Exception as e:
        print(f"Error: {e}")

def view_contacts(address_book):
    """
    Displays all contacts stored in the address book.
    If the address book is empty, it informs the user.
    """
    try:
        if not address_book:
            print("Address Book is empty.")
        else:
            print("\nContacts List:")
            for contact in address_book:
                print(f"{contact[0]} {contact[1]}, {contact[2]}, {contact[3]}, {contact[4]} {contact[5]}, {contact[6]}, {contact[7]}")  
    except Exception as e:
        print(f"Error: {e}")

def main():
    """
    Main function that runs the Address Book program.
    Provides a menu for adding and viewing contacts.
    Uses exception handling to ensure smooth execution.
    """
    address_book = []

    while True:
        try:
            print("\n1. Add Contact\n2. View Contacts\n3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                add_contact(address_book)
            elif choice == "2":
                view_contacts(address_book)
            elif choice == "3":
                print("Exiting Address Book.")
                break
            else:
                print("Invalid choice! Please try again.")
        except Exception as e:
            print(f"Unexpected error: {e}")


    """
    Displays all contacts stored in the address book.
    If the address book is empty, it informs the user.
    """
    try:
        if not address_book:
            print("Address Book is empty.")
        else:
            print("\nContacts List:")
            for contact in address_book:
                print(f"{contact[0]} {contact[1]}, {contact[2]}, {contact[3]}, {contact[4]} {contact[5]}, {contact[6]}, {contact[7]}")  
    except Exception as e:
        print(f"Error: {e}")

    """
    Main function that runs the Address Book program.
    Provides a menu for adding and viewing contacts.
    Uses exception handling to ensure smooth execution.
    """
    address_book = []

    while True:
        try:
            print("\n1. Add Contact\n2. View Contacts\n3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                add_contact(address_book)
            elif choice == "2":
                view_contacts(address_book)
            elif choice == "3":
                print("Exiting Address Book.")
                break
            else:
                print("Invalid choice! Please try again.")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Using class
class Contact:
    """
    Represents a contact in the Address Book.
    """
    def __init__(self, first_name, last_name, phone, email, address, city, state, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.phone}, {self.email}, {self.address}, {self.city}, {self.state}, {self.zip_code}"


class AddressBook:
    """
    Manages multiple contacts in the address book.
    """
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        """ Adds a new contact with validation """
        try:
            while True:
                first_name = input("Enter First Name: ").strip()
                last_name = input("Enter Last Name: ").strip()
                address = input("Enter Address: ").strip()
                city = input("Enter City: ").strip()
                state = input("Enter State: ").strip()
                phone = input("Enter Phone Number: ").strip()
                email = input("Enter Email: ").strip()

                zip_code = input("Enter Zip Code: ").strip()
                if not zip_code.isdigit():
                    print("Invalid zip code. Only numbers are allowed.")
                    continue

                if not all([first_name, last_name, phone, email, address, city, state, zip_code]):
                    raise ValueError("All fields are required.")

                self.contacts.append(Contact(first_name, last_name, phone, email, address, city, state, zip_code))
                print("\nContact added successfully!")
                
                add_more = input("Do you want to add another contact? (yes/no): ").strip().lower()
                if add_more != 'yes':
                    break
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def view_contacts(self):
        """ Displays all saved contacts """
        if not self.contacts:
            print("\nAddress Book is empty.")
        else:
            print("\nContacts List:")
            for contact in self.contacts:
                print(contact)

    def edit_contact(self, name):
        """ Edits an existing contact by full name """
        for contact in self.contacts:
            full_name = f"{contact.first_name} {contact.last_name}"
            if full_name.lower().strip() == name.lower().strip():
                print(f"\nEditing contact: {contact}")

                contact.first_name = input("Enter new First Name: ").strip() or contact.first_name
                contact.last_name = input("Enter new Last Name: ").strip() or contact.last_name
                contact.phone = input("Enter new Phone Number: ").strip() or contact.phone
                contact.email = input("Enter new Email: ").strip() or contact.email
                contact.address = input("Enter new Address: ").strip() or contact.address
                contact.city = input("Enter new City: ").strip() or contact.city
                contact.state = input("Enter new State: ").strip() or contact.state

                zip_code = input("Enter new Zip Code: ").strip()
                if zip_code.isdigit():
                    contact.zip_code = zip_code
                else:
                    print("Invalid zip code. Keeping the old one.")

                print("\nContact updated successfully!")
                return  
        
        print("\nContact not found.") 

    def delete_contact(self, name):
        """ Deletes an existing contact by full name """
        for contact in self.contacts:
            full_name = f"{contact.first_name} {contact.last_name}"
            if full_name.lower().strip() == name.lower().strip():
                self.contacts.remove(contact)
                print("\nContact deleted successfully!")
                return
        print("\nContact not found.")

def main():
    """ Runs the Address Book program with a menu. """
    address_book = AddressBook()

    while True:
        try:
            print("\n1. Add Contact\n2. View Contacts\n3. Edit Contact\n4. Delete Contact\n5. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                address_book.add_contact()
            elif choice == "2":
                address_book.view_contacts()
            elif choice == "3":
                name = input("Enter the full name of the contact to edit: ").strip()
                address_book.edit_contact(name)
            elif choice == "4":
                name = input("Enter the full name of the contact to delete: ").strip()
                address_book.delete_contact(name)
            elif choice == "5":
                print("Exiting Address Book.")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")

        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()