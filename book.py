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
    
    def to_dict(self):
        return self.__dict__
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    
class AddressBook:
    """
    Represents an Address Book containing multiple contacts.
    """
    def __init__(self, name):
        self.name = name
        self.contacts = []
        self.filename=f"{self.name}.json"
        self.filename_json=f"{self.name}.json"
        self.csv_filename = f"{self.name}.csv"
        self.load_contacts()

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
            
    def save_contacts(self):
        """ Saves contacts to a file """
        with open(self.filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)
    
    def load_contacts(self):
     """ Loads contacts from a file """
     try:
        with open(self.filename, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):  # Ensure we have a list
                self.contacts = [Contact.from_dict(contact) for contact in data]
        print(f"Contacts loaded from {self.filename}")
     except FileNotFoundError:
        self.contacts = []
        print(f"No existing file found for {self.filename}, starting fresh.")
     except json.JSONDecodeError:
        self.contacts = []
        print("Error decoding JSON file. Starting fresh.")

    def save_to_file(self, filename):
        """ Saves contacts to a specified file """
        with open(filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)
        print(f"Contacts saved to {filename}")
    
    def load_from_file(self, filename):
     """ Loads contacts from a specified file """
     try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):  # Ensure data is a list
                self.contacts = [Contact.from_dict(contact) for contact in data]
            print(f"Contacts successfully loaded from {filename}")
     except FileNotFoundError:
        print("File not found. No contacts loaded.")
     except json.JSONDecodeError:
        print("Error decoding JSON file. No contacts loaded.")
        
    def save_to_csv(self):
        """ Saves contacts to a CSV file """
        try:
            with open(self.csv_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["First Name", "Last Name", "Phone", "Email", "Address", "City", "State", "Zip Code"])
                for contact in self.contacts:
                    writer.writerow([contact.first_name, contact.last_name, contact.phone, contact.email, 
                                     contact.address, contact.city, contact.state, contact.zip_code])
            print(f"Contacts saved to {self.csv_filename}")
        except Exception as e:
            print(f"Error saving to CSV: {e}")
    
    def load_from_csv(self):
        """ Loads contacts from a CSV file """
        try:
            with open(self.csv_filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                self.contacts = [Contact(*row) for row in reader]
            print(f"Contacts loaded from {self.csv_filename}")
        except FileNotFoundError:
            print(f"CSV file {self.csv_filename} not found. Starting fresh.")
        except Exception as e:
            print(f"Error loading from CSV: {e}")
    
    def save_to_json(self):
        """ Saves contacts to a JSON file """
        with open(self.filename_json, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)
        print(f"Contacts saved to {self.filename_json}")
    
    def load_contacts(self):
        """ Loads contacts from JSON file """
        try:
            with open(self.filename_json, 'r') as file:
                data = json.load(file)
                self.contacts = [Contact.from_dict(contact) for contact in data]
            print(f"Contacts loaded from {self.filename_json}")
        except (FileNotFoundError, json.JSONDecodeError):
            print("No existing JSON file found, starting fresh.")
            
    def search_city(self,city):
        """
        search and display by particular city
        """
        match=[contact for contact in self.contacts if contact.city.lower()==city.lower()]
        if match:
            print(f"contact found in {city}:")
        else:
            print(f"no contacts found in {city}:")
            
    
    def view_state(self,state):
        """
        view person by state        
        """
        match=[contact for contact in self.contacts if contact.state.lower()==state.lower()]
        if match:
            print(f"contact found in {state}:")
        else:
            print(f"no contacts found in {state}:")
    
    def count_city(self,city):
        """
        count contacts in city
        """
        count=sum(1 for contact in self.contacts if contact.city.lower()==city.lower())
        print(f"number of contact in {city}:{count}")
    
    def count_state(self,state):
        """
        count contact in state
        """        
        count=sum(1 for contact in self.contacts if contact.state.lower()==state.lower())
        print(f"number of contact in {state}:{count}")
    
    def sort_contacts(self):
        """ Sort contacts alphabetically by first name, then last name """
        def compare(contact):
            return contact.first_name.lower(), contact.last_name.lower()       
        self.contacts.sort(key=compare)
    
    def sort_by_zip(self):
        """ Sorts contacts numerically by zip code """
        def compare_zip(contact):
            return int(contact.zip_code)
        self.contacts.sort(key=compare_zip)
        
    def view_contacts(self,sort_by="name"):
        """ Displays all saved contacts """
        if not self.contacts:
            print("\nAddress Book is empty.")
        else:
            if sort_by == "zip":
                self.sort_by_zip()
            else:
                self.sort_contacts()
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

    def get_address_book(self, name):
        return self.address_books.get(name)

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
                        print("\nNo Address Book selected.")
                
                elif choice == "6":
                    if self.current_book:
                        state = input("Enter state name to view: ").strip()
                        self.current_book.view_state(state)
                    else:
                        print("\nNo Address Book selected.")
                elif choice == "7":
                    if self.current_book:
                        city = input("Enter city name to count contacts: ").strip()
                        self.current_book.count_city(city)
                    else:
                        print("\nNo Address Book selected.")
                elif choice == "8":
                    if self.current_book:
                        state = input("Enter state name to count contacts: ").strip()
                        self.current_book.count_state(state)
                    else:
                        print("\nNo Address Book selected.")
                elif choice == "9":
                    if self.current_book:
                        sort = input("search alphabetcally:").strip()
                        self.current_book.sort_contacts(sort)
                    else:
                        print("\nNo Address Book selected.")
                elif choice == "10":
                    if self.current_book:
                        sort_zip = input("search by zip:").strip()
                        self.current_book.sort_by_zip(sort_zip)
                    else:
                        print("\nNo Address Book selected.")
                
                elif choice == "11":
                    book_name = input("Enter Address Book name: ").strip()
                    address_book = self.get_address_book(book_name)
                    if address_book:
                        filename = input("Enter filename to save to (e.g., 'book.txt'): ").strip()
                        address_book.save_to_file(filename)
                    else:
                        print(f"Address Book '{book_name}' does not exist!")
                
                elif choice == "12":
                    book_name = input("Enter Address Book name: ").strip()
                    address_book = self.get_address_book(book_name)
                    if address_book:
                        filename = input("Enter filename to load from (e.g., 'book.txt'): ").strip()
                        address_book.load_from_file(filename)
                    else:
                        print(f"Address Book '{book_name}' does not exist!")
                        
                elif choice == "13":
                    if self.current_book:
                        self.current_book.save_to_csv()
                    else:
                        print("No Address Book selected.")
               
                elif choice == "14":
                    if self.current_book:
                        self.current_book.load_from_csv()
                    else:
                        print("No Address Book selected.")
                
                elif choice == "15":
                    if self.current_book:
                        self.current_book.save_to_json()
                    else:
                        print("No Address Book selected.")
               
                elif choice == "16":
                    if self.current_book:
                        self.current_book.load_contacts()
                    else:
                        print("No Address Book selected.")
        
                elif choice == "17":
                    print("Exiting Address Book System.")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1 and 13.")
            except Exception as e:
                print(f"Unexpected error: {e}")

if __name__ == "__main__":
    system = AddressBookSystem()
    system.main_menu()
