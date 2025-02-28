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

import json
import csv
import logging

# Configure logging at the start of the program
logging.basicConfig(
    filename='address_book.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Original functions from first part (with logging)
def add_contact(address_book):
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
        logger.info("Contact added successfully")
    
    except Exception as e:
        logger.error(f"Error adding contact: {e}")

def view_contacts(address_book):
    try:
        if not address_book:
            logger.info("Address Book is empty")
        else:
            logger.info("Displaying Contacts List")
            for contact in address_book:
                logger.info(f"{contact[0]} {contact[1]}, {contact[2]}, {contact[3]}, {contact[4]} {contact[5]}, {contact[6]}, {contact[7]}")  
    except Exception as e:
        logger.error(f"Error viewing contacts: {e}")

def main():
    address_book = []
    logger.info("Starting Address Book program")

    while True:
        try:
            print("\n1. Add Contact\n2. View Contacts\n3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                add_contact(address_book)
            elif choice == "2":
                view_contacts(address_book)
            elif choice == "3":
                logger.info("Exiting Address Book program")
                break
            else:
                logger.warning("Invalid choice entered")
        except Exception as e:
            logger.error(f"Unexpected error in main loop: {e}")

class Contact:
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
    
    def to_dict(self):
        return self.__dict__
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []
        self.filename = f"{self.name}.json"
        self.filename_json = f"{self.name}.json"
        self.csv_filename = f"{self.name}.csv"
        logger.info(f"Initializing AddressBook: {name}")
        self.load_contacts()

    def add_contact(self):
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
            
            for contact in self.contacts:
                if contact.first_name == first_name and contact.last_name == last_name and contact.phone == phone:
                    raise ValueError("Duplicate contact found - person already exists")
            
            self.contacts.append(Contact(first_name, last_name, phone, email, address, city, state, zip_code))
            logger.info(f"Contact added successfully to {self.name}: {first_name} {last_name}")
        except ValueError as e:
            logger.warning(f"Validation error adding contact: {e}")
        except Exception as e:
            logger.error(f"Unexpected error adding contact: {e}")

    def save_contacts(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)
            logger.info(f"Contacts saved to {self.filename}")
        except Exception as e:
            logger.error(f"Error saving contacts: {e}")

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    self.contacts = [Contact.from_dict(contact) for contact in data]
                logger.info(f"Contacts loaded from {self.filename}")
        except FileNotFoundError:
            self.contacts = []
            logger.info(f"No existing file found for {self.filename}, starting fresh")
        except json.JSONDecodeError:
            self.contacts = []
            logger.error(f"Error decoding JSON file {self.filename}, starting fresh")

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)
            logger.info(f"Contacts saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    self.contacts = [Contact.from_dict(contact) for contact in data]
                logger.info(f"Contacts successfully loaded from {filename}")
        except FileNotFoundError:
            logger.warning(f"File not found: {filename}. No contacts loaded")
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON file {filename}. No contacts loaded")

    def save_to_csv(self):
        try:
            with open(self.csv_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["First Name", "Last Name", "Phone", "Email", "Address", "City", "State", "Zip Code"])
                for contact in self.contacts:
                    writer.writerow([contact.first_name, contact.last_name, contact.phone, contact.email, 
                                   contact.address, contact.city, contact.state, contact.zip_code])
            logger.info(f"Contacts saved to {self.csv_filename}")
        except Exception as e:
            logger.error(f"Error saving to CSV: {e}")

    def load_from_csv(self):
        try:
            with open(self.csv_filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                self.contacts = [Contact(*row) for row in reader]
            logger.info(f"Contacts loaded from {self.csv_filename}")
        except FileNotFoundError:
            logger.info(f"CSV file {self.csv_filename} not found. Starting fresh")
        except Exception as e:
            logger.error(f"Error loading from CSV: {e}")

    def save_to_json(self):
        try:
            with open(self.filename_json, 'w') as file:
                json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)
            logger.info(f"Contacts saved to {self.filename_json}")
        except Exception as e:
            logger.error(f"Error saving to JSON: {e}")

    def search_city(self, city):
        match = [contact for contact in self.contacts if contact.city.lower() == city.lower()]
        if match:
            logger.info(f"Contacts found in {city}: {len(match)} matches")
            print(f"\nContacts found in {city}:")
            for contact in match:
                print(contact)
        else:
            logger.info(f"No contacts found in {city}")
            print(f"\nNo contacts found in {city}")

    def view_state(self, state):
        match = [contact for contact in self.contacts if contact.state.lower() == state.lower()]
        if match:
            logger.info(f"Contacts found in {state}: {len(match)} matches")
            print(f"\nContacts found in {state}:")
            for contact in match:
                print(contact)
        else:
            logger.info(f"No contacts found in {state}")
            print(f"\nNo contacts found in {state}")

    def count_city(self, city):
        count = sum(1 for contact in self.contacts if contact.city.lower() == city.lower())
        logger.info(f"Number of contacts in {city}: {count}")

    def count_state(self, state):
        count = sum(1 for contact in self.contacts if contact.state.lower() == state.lower())
        logger.info(f"Number of contacts in {state}: {count}")
        print(f"\nNumber of contacts in {state}: {count}")

    def sort_contacts(self):
        def compare(contact):
            return contact.first_name.lower(), contact.last_name.lower()       
        self.contacts.sort(key=compare)
        logger.info(f"Contacts sorted alphabetically in {self.name}")

    def sort_by_zip(self):
        def compare_zip(contact):
            return int(contact.zip_code)
        self.contacts.sort(key=compare_zip)
        logger.info(f"Contacts sorted by zip code in {self.name}")
        print(f"\nContacts sorted by zip code in {self.name}")

    def view_contacts(self, sort_by="name"):
        if not self.contacts:
            logger.info(f"Address Book {self.name} is empty")
            print(f"\nAddress Book {self.name} is empty")
        else:
            if sort_by == "zip":
                self.sort_by_zip()
            else:
                self.sort_contacts()
            logger.info(f"Displaying contacts in {self.name}")
            for contact in self.contacts:
                print(contact)
                logger.info(str(contact))

class AddressBookSystem:
    def __init__(self):
        self.address_books = {}
        self.current_book = None
        logger.info("AddressBookSystem initialized")

    def get_address_book(self, name):
        return self.address_books.get(name)

    def create_address_book(self):
        try:
            name = input("Enter Address Book Name: ").strip()
            if name in self.address_books:
                raise ValueError("Address Book with this name already exists")
            self.address_books[name] = AddressBook(name)
            self.current_book = self.address_books[name]
            logger.info(f"Address Book '{name}' created and set as active")
        except ValueError as e:
            logger.warning(f"Error creating address book: {e}")
        except Exception as e:
            logger.error(f"Unexpected error creating address book: {e}")

    def switch_address_book(self):
        try:
            name = input("Enter Address Book Name to Switch To: ").strip()
            if name not in self.address_books:
                raise ValueError("Address Book not found")
            self.current_book = self.address_books[name]
            logger.info(f"Switched to Address Book '{name}'")
        except ValueError as e:
            logger.warning(f"Error switching address book: {e}")
        except Exception as e:
            logger.error(f"Unexpected error switching address book: {e}")

    def main_menu(self):
        logger.info("Starting main menu")
        while True:
            try:
                print("\n1. Create Address Book\n2. Switch Address Book\n3. Add Contact\n4. View Contacts  \n5. Search by City \n6. view by state  \n7. count contact by city  \n8. count contact by state \n9.sort alphabetically \n10. sort by zip \n11.Save address book \n12.Load address book \n13. Save to csv  \n14. Load from csv \n15.Save to json  \n16. load from json \n17. Exit")
                choice = input("Choose an option: ").strip()

                if choice == "1":
                    self.create_address_book()
                elif choice == "2":
                    self.switch_address_book()
                elif choice == "3":
                    if self.current_book:
                        self.current_book.add_contact()
                    else:
                        logger.warning("No Address Book selected for adding contact")
                elif choice == "4":
                    if self.current_book:
                        self.current_book.view_contacts()
                    else:
                        logger.warning("No Address Book selected for viewing contacts")
                elif choice == "5":
                    if self.current_book:
                        city = input("Enter city name to search: ").strip()
                        self.current_book.search_city(city)
                    else:
                        logger.warning("No Address Book selected for city search")
                elif choice == "6":
                    if self.current_book:
                        state = input("Enter state name to view: ").strip()
                        self.current_book.view_state(state)
                    else:
                        logger.warning("No Address Book selected for state view")
                elif choice == "7":
                    if self.current_book:
                        city = input("Enter city name to count contacts: ").strip()
                        self.current_book.count_city(city)
                    else:
                        logger.warning("No Address Book selected for city count")
                elif choice == "8":
                    if self.current_book:
                        state = input("Enter state name to count contacts: ").strip()
                        self.current_book.count_state(state)
                    else:
                        logger.warning("No Address Book selected for state count")
                elif choice == "9":
                    if self.current_book:
                        self.current_book.sort_contacts()
                    else:
                        logger.warning("No Address Book selected for sorting")
                elif choice == "10":
                    if self.current_book:
                        self.current_book.sort_by_zip()
                    else:
                        logger.warning("No Address Book selected for zip sorting")
                elif choice == "11":
                    book_name = input("Enter Address Book name: ").strip()
                    address_book = self.get_address_book(book_name)
                    if address_book:
                        filename = input("Enter filename to save to (e.g., 'book.txt'): ").strip()
                        address_book.save_to_file(filename)
                    else:
                        logger.warning(f"Address Book '{book_name}' does not exist for saving")
                elif choice == "12":
                    book_name = input("Enter Address Book name: ").strip()
                    address_book = self.get_address_book(book_name)
                    if address_book:
                        filename = input("Enter filename to load from (e.g., 'book.txt'): ").strip()
                        address_book.load_from_file(filename)
                    else:
                        logger.warning(f"Address Book '{book_name}' does not exist for loading")
                elif choice == "13":
                    if self.current_book:
                        self.current_book.save_to_csv()
                    else:
                        logger.warning("No Address Book selected for CSV save")
                elif choice == "14":
                    if self.current_book:
                        self.current_book.load_from_csv()
                    else:
                        logger.warning("No Address Book selected for CSV load")
                elif choice == "15":
                    if self.current_book:
                        self.current_book.save_to_json()
                    else:
                        logger.warning("No Address Book selected for JSON save")
                elif choice == "16":
                    if self.current_book:
                        self.current_book.load_contacts()
                    else:
                        logger.warning("No Address Book selected for JSON load")
                elif choice == "17":
                    logger.info("Exiting Address Book System")
                    break
                else:
                    logger.warning(f"Invalid menu choice: {choice}")
            except Exception as e:
                logger.error(f"Unexpected error in main menu: {e}")

if __name__ == "__main__":
    system = AddressBookSystem()
    system.main_menu()