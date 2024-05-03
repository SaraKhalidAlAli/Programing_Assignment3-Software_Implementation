#adding the classes
import pickle
class Employee:
    #attributes for employee
    def __init__(self, name, emp_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details

    # Getter, setter methods:
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_emp_id(self):
        return self.emp_id
    def set_emp_id(self, emp_id):
        self.emp_id = emp_id
    def get_department(self):
        return self.department
    def set_department(self, department):
        self.department = department
    def get_job_title(self):
        return self.job_title
    def set_job_title(self, job_title):
        self.job_title = job_title
    def get_basic_salary(self):
        return self.basic_salary
    def set_basic_salary(self, basic_salary):
        self.basic_salary = basic_salary
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
    def get_date_of_birth(self):
        return self.date_of_birth
    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth
    def get_passport_details(self):
        return self.passport_details
    def set_passport_details(self, passport_details):
        self.passport_details = passport_details


class Client:
    #attributes for the clients and initializing
    def __init__(self, client_id, name, address, phone_number, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.budget = budget

    # Getter, setter methods:
    def get_client_id(self):
        return self.client_id
    def set_client_id(self, client_id):
        self.client_id = client_id
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_phone_number(self):
        return self.phone_number
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    def get_budget(self):
        return self.budget
    def set_budget(self, budget):
        self.budget = budget


class Event:
    #attributes for the Event and initializing it
    def __init__(self, event_id, event_type, theme, date, time, duration, venue, client_id, guest_list):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue = venue
        self.client_id = client_id
        self.guest_list = guest_list

    # Getter, setter methods:
    def get_event_id(self):
        return self.event_id
    def set_event_id(self, event_id):
        self.event_id = event_id
    def get_event_type(self):
        return self.event_type
    def set_event_type(self, event_type):
        self.event_type = event_type
    def get_theme(self):
        return self.theme
    def set_theme(self, theme):
        self.theme = theme
    def get_date(self):
        return self.date
    def set_date(self, date):
        self.date = date
    def get_time(self):
        return self.time
    def set_time(self, time):
        self.time = time
    def get_duration(self):
        return self.duration
    def set_duration(self, duration):
        self.duration = duration
    def get_venue(self):
        return self.venue
    def set_venue(self, venue):
        self.venue = venue
    def get_client_id(self):
        return self.client_id
    def set_client_id(self, client_id):
        self.client_id = client_id
    def get_guest_list(self):
        return self.guest_list
    def set_guest_list(self, guest_list):
        self.guest_list = guest_list

class Guest:
    #attributes for the Guest and initializing it
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    # Getter , setter methods:
    def get_guest_id(self):
        return self.guest_id
    def set_guest_id(self, guest_id):
        self.guest_id = guest_id
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_contact_details(self):
        return self.contact_details
    def set_contact_details(self, contact_details):
        self.contact_details = contact_details

class Venue:
    # attributes for the Venue and initializing it
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    # Getter, setter methods:
    def get_venue_id(self):
        return self.venue_id
    def set_venue_id(self, venue_id):
        self.venue_id = venue_id
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_contact(self):
        return self.contact
    def set_contact(self, contact):
        self.contact = contact
    def get_min_guests(self):
        return self.min_guests
    def set_min_guests(self, min_guests):
        self.min_guests = min_guests
    def get_max_guests(self):
        return self.max_guests
    def set_max_guests(self, max_guests):
        self.max_guests = max_guests

class Supplier:
    # attributes for the Supplier and initializing it
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    # Getter, setter methods:
    def get_supplier_id(self):
        return self.supplier_id
    def set_supplier_id(self, supplier_id):
        self.supplier_id = supplier_id
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_contact_details(self):
        return self.contact_details
    def set_contact_details(self, contact_details):
        self.contact_details = contact_details

class Caterer(Supplier):
    # attributes for the Caterer and initializing it
    def __init__(self, supplier_id, name, address, contact_details, menu, min_guests, max_guests):
        super().__init__(supplier_id, name, address, contact_details)
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests

    # Getter, setter methods to Caterer:
    def get_menu(self):
        return self.menu
    def set_menu(self, menu):
        self.menu = menu
    def get_min_guests(self):
        return self.min_guests
    def set_min_guests(self, min_guests):
        self.min_guests = min_guests
    def get_max_guests(self):
        return self.max_guests
    def set_max_guests(self, max_guests):
        self.max_guests = max_guests



# Pickling functions for the classes above:

    """Save an object to a file using pickle.
    Args:
        obj (object): The Python object to pickle.
        filename (str): The file path where the object will be saved."""
def save_object(obj, filename):
    with open(filename, 'wb') as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

    """ Load an object from a pickle file.
    Args:
        filename (str): The file path from where the object will be loaded.
    Returns: object: The unpickled Python object."""
def load_object(filename):
    #Load an object from a pickle file.
    with open(filename, 'rb') as inp:
        return pickle.load(inp)


# adding exmaple usages for classes
if __name__ == "__main__":
    # Employee example
    employee = Employee("John Doe", "E001", "Marketing", "Manager", 50000, 35, "1985-07-12", "XP23456")
    save_object(employee, 'employee.pkl')
    loaded_employee = load_object('employee.pkl')
    print(f"Loaded Employee: {loaded_employee.get_name()}, Department: {loaded_employee.get_department()}")

    # Client example
    client = Client("C002", "Alice Smith", "456 Park Ave", "555-2345", 2000)
    save_object(client, 'client.pkl')
    loaded_client = load_object('client.pkl')
    print(f"Loaded Client: {loaded_client.get_name()}, Phone: {loaded_client.get_phone_number()}")

    # Event example
    event = Event("EV103", "Conference", "Tech", "2023-10-25", "09:00", 8, "Convention Center", "C002", ["G103", "G104"])
    save_object(event, 'event.pkl')
    loaded_event = load_object('event.pkl')
    print(f"Loaded Event: {loaded_event.get_event_type()}, Venue: {loaded_event.get_venue()}")
    # Additional examples for Guest, Venue, Supplier, and Caterer can be added following the same pattern.
