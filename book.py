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

# Using class
class Contact:
    """
    Represents a contact in the Address Book.
    """
    def __init__(self, first_name, last_name, phone, email, address, city, state, zip_code):
        """
        Initializes contact details.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __str__(self):
        """
        Returns a formatted string representation of the contact.
        """
        return f"{self.first_name}, {self.last_name}, {self.phone}, {self.email}, {self.address}, {self.city}, {self.state}, {self.zip_code}"

class AddressBook:
    """
    Manages multiple contacts in the address book.
    """   
    def __init__(self):
        """
        Initializes an empty contact list.
        """
        self.contacts = []

    def add_contact(self):
        """
        Adds a new contact with error handling.
        """
        try:
            first_name = input("Enter First Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            address = input("Enter Address: ").strip()
            city = input("Enter City: ").strip()
            state = input("Enter State: ").strip()
            phone = input("Enter Phone Number: ").strip()
            email = input("Enter Email: ").strip()

            while True:
                zip_code = input("Enter Zip Code: ").strip()
                if zip_code.isdigit():
                    break
                else:
                    print("Invalid zip code. Only numbers are allowed.")

            if not all([first_name, last_name, phone, email, address, city, state, zip_code]):
                raise ValueError("All fields are required.")

            contact = Contact(first_name, last_name, phone, email, address, city, state, zip_code)
            self.contacts.append(contact)
            print("\nContact added successfully!")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def view_contacts(self):
        """
        Displays all saved contacts.
        """
        if not self.contacts:
            print("\nAddress Book is empty.")
        else:
            print("\nContacts List:")
            for contact in self.contacts:
                print(contact)

    def edit_contact(self, name):
        """
        edits an existing contact by full name.
        """
        for contact in self.contacts:
            full_name = f"{contact.first_name} {contact.last_name}"
            if full_name.lower() == name.lower():
                print(f"\nEditing contact: {contact}")

                # Get updated values while keeping existing values if left blank
                new_first_name = input("Enter new First Name:").strip() or contact.first_name
                new_last_name = input("Enter new Last Name:").strip() or contact.last_name
                new_phone = input("Enter new Phone Number:").strip() or contact.phone
                new_email = input("Enter new Email:").strip() or contact.email
                new_address = input("Enter new Address:").strip() or contact.address
                new_city = input("Enter new City:").strip() or contact.city
                new_state = input("Enter new State:").strip() or contact.state

                while True:
                    new_zip_code = input("Enter new Zip Code (leave blank to keep existing): ").strip() or contact.zip_code
                    if new_zip_code.isdigit():
                        break
                    print("Invalid zip code. Only numbers are allowed.")

                # Update contact details
                contact.first_name = new_first_name
                contact.last_name = new_last_name
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                contact.city = new_city
                contact.state = new_state
                contact.zip_code = new_zip_code

                print("\nContact updated successfully!")
                return  # Exit after updating

        print("\nContact not found.")  # If no match is found

def main():
    """Runs the Address Book program with a menu."""
    address_book = AddressBook()

    while True:
        try:
            print("\n1️. Add Contact\n2️. View Contacts\n3️. Edit Contact\n4️. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                address_book.add_contact()
            elif choice == "2":
                address_book.view_contacts()
            elif choice == "3":
                name = input("Enter the full name of the contact to edit: ").strip()
                address_book.edit_contact(name)
            elif choice == "4":
                print("Exiting Address Book.")
                break
            else:
                print("Invalid choice! Please enter 1, 2, 3, or 4.")

        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

