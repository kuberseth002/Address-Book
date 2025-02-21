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
    Represents an Address Book containing multiple contacts.
    """
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def add_contact(self):
        """ Adds a new contact with validation """
        try:
            first_name = input("Enter First Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            phone = input("Enter Phone Number: ").strip()
            email = input("Enter Email: ").strip()
            address = input("Enter Address: ").strip()
            city = input("Enter City: ").strip()
            state = input("Enter State: ").strip()
            zip_code = input("Enter Zip Code: ").strip()

            if not zip_code.isdigit():
                raise ValueError("Invalid zip code. Only numbers are allowed.")

            if not all([first_name, last_name, phone, email, address, city, state, zip_code]):
                raise ValueError("All fields are required.")
            
            # check duplicate
            for contact in self.contacts:
                if contact.first_name==first_name and contact.last_name==last_name and contact.phone==phone:
                    raise ValueError("duplicate contact found person already exist")
            self.contacts.append(Contact(first_name, last_name, phone, email, address, city, state, zip_code))
            print("\nContact added successfully!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
    
    def search_city(self,city):
        """
        search and display by particular city
        """
        match=[contact for contact in self.contacts if contact.city.lower()==city.lower()]
        if match:
            print(f"contact found in {city}:")
        else:
            print(f"no contacts found in {city}:")

    def view_contacts(self):
        """ Displays all saved contacts """
        if not self.contacts:
            print("\nAddress Book is empty.")
        else:
            print(f"\nContacts in {self.name}:")
            for contact in self.contacts:
                print(contact)

class AddressBookSystem:
    """
    Manages multiple Address Books.
    """
    def __init__(self):
        self.address_books = {}
        self.current_book = None

    def create_address_book(self):
     """ Creates a new Address Book and selects it as current """
     try:
        name = input("Enter Address Book Name: ").strip()
        if name in self.address_books:
            raise ValueError("Address Book with this name already exists.")
        self.address_books[name] = AddressBook(name)
        self.current_book = self.address_books[name]  # Auto-select the newly created book
        print(f"\nAddress Book '{name}' created successfully and set as active!")
     except ValueError as e:
        print(f"Error: {e}")
     except Exception as e:
        print(f"Unexpected Error: {e}")

    def switch_address_book(self):
        """ Switches to another Address Book """
        try:
            name = input("Enter Address Book Name to Switch To: ").strip()
            if name not in self.address_books:
                raise ValueError("Address Book not found.")
            self.current_book = self.address_books[name]
            print(f"\nSwitched to Address Book '{name}'")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def main_menu(self):
        """ Runs the Address Book System with a menu """
        while True:
            try:
                print("\n1. Create Address Book\n2. Switch Address Book\n3. Add Contact\n4. View Contacts  \n5. Search by City \n6. Exit")
                choice = input("Choose an option: ").strip()

                if choice == "1":
                    self.create_address_book()
                elif choice == "2":
                    self.switch_address_book()
                elif choice == "3":
                    if self.current_book:
                        self.current_book.add_contact()
                    else:
                        print("\nNo Address Book selected. Please switch to one first.")
                elif choice == "4":
                    if self.current_book:
                        self.current_book.view_contacts()
                    else:
                        print("\nNo Address Book selected. Please switch to one first.")
                elif choice == "5":
                    if self.current_book:
                        city = input("Enter city name to search: ").strip()
                        self.current_book.search_city(city)
                    else:
                        print("\nNo Address Book selected. Please switch to one first.")
                elif choice == "6":
                    print("Exiting Address Book System.")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1 and 5.")
            except Exception as e:
                print(f"Unexpected error: {e}")

if __name__ == "__main__":
    system = AddressBookSystem()
    system.main_menu()
