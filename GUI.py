import tkinter as tk
from tkinter import messagebox

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Event Management System")

        # Initialize storage lists and dictionaries
        self.employee_list = []
        self.client_data = {}
        self.supplier_list = []
        self.guest_data = {}
        self.venue_list = []

        # Employee management buttons
        self.employee_button = tk.Button(master, text="Add Employee", command=self.open_employee_window)
        self.employee_button.grid(row=0, column=0, padx=10, pady=5)
        self.display_employee_button = tk.Button(master, text="Display Employees", command=self.open_display_employee_window)
        self.display_employee_button.grid(row=0, column=1, padx=10, pady=5)
        self.delete_employee_button = tk.Button(master, text="Delete Employee", command=self.open_delete_employee_window)
        self.delete_employee_button.grid(row=0, column=2, padx=10, pady=5)

        # Client management buttons
        self.client_button = tk.Button(master, text="Add Client and Event info", command=self.open_client_window)
        self.client_button.grid(row=1, column=0, padx=10, pady=5)
        self.display_client_button = tk.Button(master, text="Display Clients and Event Preference", command=self.open_display_client_window)
        self.display_client_button.grid(row=1, column=1, padx=10, pady=5)
        self.delete_client_button = tk.Button(master, text="Delete Client and Event", command=self.open_delete_client_window)
        self.delete_client_button.grid(row=1, column=2, padx=10, pady=5)

        # Supplier management buttons
        self.supplier_button = tk.Button(master, text="Add Supplier", command=self.open_supplier_window)
        self.supplier_button.grid(row=2, column=0, padx=10, pady=5)
        self.display_supplier_button = tk.Button(master, text="Display Suppliers", command=self.open_display_supplier_info_window)
        self.display_supplier_button.grid(row=2, column=1, padx=10, pady=5)
        self.delete_supplier_button = tk.Button(master, text="Delete Supplier", command=self.open_delete_supplier_window)
        self.delete_supplier_button.grid(row=2, column=2, padx=10, pady=5)

        # Guest management buttons
        self.guest_button = tk.Button(master, text="Add Guest", command=self.open_guest_window)
        self.guest_button.grid(row=3, column=0, padx=10, pady=5)
        self.display_guest_button = tk.Button(master, text="Display Guests", command=self.open_display_guest_info_window)
        self.display_guest_button.grid(row=3, column=1, padx=10, pady=5)
        self.delete_guest_button = tk.Button(master, text="Delete Guest", command=self.open_delete_guest_window)
        self.delete_guest_button.grid(row=3, column=2, padx=10, pady=5)

        # Venue management buttons
        self.venue_button = tk.Button(master, text="Add Venue", command=self.open_venue_window)
        self.venue_button.grid(row=4, column=0, padx=10, pady=5)
        self.display_venue_button = tk.Button(master, text="Display Venues", command=self.open_display_venue_info_window)
        self.display_venue_button.grid(row=4, column=1, padx=10, pady=5)
        self.delete_venue_button = tk.Button(master, text="Delete Venue", command=self.open_delete_venue_window)
        self.delete_venue_button.grid(row=4, column=2, padx=10, pady=5)

        # Inside the __init__ method of MainWindow class:
        self.modify_employee_button = tk.Button(master, text="Modify Employee", command=self.open_modify_employee_window)
        self.modify_employee_button.grid(row=0, column=3, padx=10, pady=5)
        self.modify_client_button = tk.Button(master, text="Modify Client", command=self.open_modify_client_window)
        self.modify_client_button.grid(row=1, column=3, padx=10, pady=5)
        self.modify_supplier_button = tk.Button(master, text="Modify Supplier", command=self.open_modify_supplier_window)
        self.modify_supplier_button.grid(row=2, column=3, padx=10, pady=5)
        self.modify_guest_button = tk.Button(master, text="Modify Guest", command=self.open_modify_guest_window)
        self.modify_guest_button.grid(row=3, column=3, padx=10, pady=5)
        self.modify_venue_button = tk.Button(master, text="Modify Venue", command=self.open_modify_venue_window)
        self.modify_venue_button.grid(row=4, column=3, padx=10, pady=5)

        # Status bar for feedback
        self.status_bar = tk.Label(master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.grid(row=6, column=0, columnspan=3, sticky=tk.W + tk.E)

    # Methods for opening each window should be defined similarly to existing methods
    def open_delete_employee_window(self):
        # Opens a new window to delete an existing employee.
        delete_employee_window = tk.Toplevel(self.master)
        DeleteEmployeeWindow(delete_employee_window, self.employee_list, self.status_bar)

    def open_delete_client_window(self):
        # Opens a new window to delete an existing client and their event information.
        delete_client_window = tk.Toplevel(self.master)
        DeleteClientWindow(delete_client_window, self.client_data, self.status_bar)

    def open_delete_supplier_window(self):
        # Opens a new window to delete a supplier from the system.
        delete_supplier_window = tk.Toplevel(self.master)
        DeleteSupplierWindow(delete_supplier_window, self.supplier_list, self.status_bar)

    def open_delete_guest_window(self):
        # Opens a new window to delete a guest from an event.
        delete_guest_window = tk.Toplevel(self.master)
        DeleteGuestWindow(delete_guest_window, self.guest_data, self.status_bar)

    def open_delete_venue_window(self):
        # Opens a new window to delete a venue from the list of available venues.
        delete_venue_window = tk.Toplevel(self.master)
        DeleteVenueWindow(delete_venue_window, self.venue_list, self.status_bar)


    def open_employee_window(self):
        # Opens a new window to add a new employee.
        employee_window = tk.Toplevel(self.master)
        EmployeeWindow(employee_window, self.employee_list)

    def open_display_employee_window(self):
        # Opens a new window to display information about existing employees.
        display_employee_window = tk.Toplevel(self.master)
        DisplayEmployeeWindow(display_employee_window, self.employee_list)

    def open_client_window(self):
        # Opens a new window to add a new client and their event information.
        client_window = tk.Toplevel(self.master)
        ClientWindow(client_window, self.client_data)

    def open_display_client_window(self):
        # Opens a new window to display details about clients and their event preferences.
        display_client_window = tk.Toplevel(self.master)
        DisplayClientWindow(display_client_window, self.client_data)

    def open_guest_window(self):
        # Opens a new window to add a new guest to an event.
        guest_window = tk.Toplevel(self.master)
        GuestWindow(guest_window, self.client_data)

    def open_display_guest_info_window(self):
        # Opens a new window to display information about guests.
        display_guest_info_window = tk.Toplevel(self.master)
        DisplayGuestInfoWindow(display_guest_info_window, self.client_data)

    def open_supplier_window(self):
        # Opens a new window to add a new supplier.
        self.supplier_window = tk.Toplevel(self.master)
        SupplierWindow(self.supplier_window, self.supplier_list, event_options=["Event 1", "Event 2"])

    def open_display_supplier_info_window(self):
        # Opens a new window to display supplier details.
        display_supplier_info_window = tk.Toplevel(self.master)
        DisplaySupplierInfoWindow(display_supplier_info_window, self.supplier_list)

    def open_venue_window(self):
        # Opens a new window to add a new venue.
        venue_window = tk.Toplevel(self.master)
        VenueWindow(venue_window, self.venue_list)

    def open_display_venue_info_window(self):
        # Opens a new window to display information about venues.
        display_venue_info_window = tk.Toplevel(self.master)
        DisplayVenueInfoWindow(display_venue_info_window, self.venue_list)


    def open_modify_employee_window(self):
        # Opens a new window to modify existing employee information.
        modify_window = tk.Toplevel(self.master)
        ModifyEmployeeWindow(modify_window, self.employee_list, self.status_bar)

    def open_modify_client_window(self):
        # Opens a new window to modify existing client and event information.
        modify_window = tk.Toplevel(self.master)
        ModifyClientWindow(modify_window, self.client_data, self.status_bar)

    def open_modify_supplier_window(self):
        # Opens a new window to modify details of an existing supplier.
        modify_window = tk.Toplevel(self.master)
        ModifySupplierWindow(modify_window, self.supplier_list, self.status_bar)

    def open_modify_guest_window(self):
        # Opens a new window to modify information about an existing guest.
        modify_window = tk.Toplevel(self.master)
        ModifyGuestWindow(modify_window, self.guest_data, self.status_bar)

    def open_modify_venue_window(self):
        # Opens a new window to modify details of an existing venue.
        modify_window = tk.Toplevel(self.master)
        ModifyVenueWindow(modify_window, self.venue_list, self.status_bar)

#adding the logic to make the button work:
class EmployeeWindow:
    def __init__(self, master, employee_list):
        self.master = master
        self.master.title("Add Employee")
        self.employee_list = employee_list

        # Labels and entry fields for attributes
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.emp_id_label = tk.Label(master, text="Employee ID:")
        self.emp_id_label.grid(row=1, column=0, padx=10, pady=5)
        self.emp_id_entry = tk.Entry(master)
        self.emp_id_entry.grid(row=1, column=1, padx=10, pady=5)

        self.job_title_label = tk.Label(master, text="Job Title:")
        self.job_title_label.grid(row=2, column=0, padx=10, pady=5)
        self.job_title_var = tk.StringVar(master)
        self.job_title_var.set("Manager")  # Default job title
        self.job_title_optionmenu = tk.OptionMenu(master, self.job_title_var, "Manager", "Salesperson")
        self.job_title_optionmenu.grid(row=2, column=1, padx=10, pady=5)

        # Button to save employee data
        self.save_button = tk.Button(master, text="Save", command=self.save_employee)
        self.save_button.grid(row=3, columnspan=2, padx=10, pady=5)

    def save_employee(self):
        # Retrieve data from entry fields
        name = self.name_entry.get()
        emp_id = self.emp_id_entry.get()
        job_title = self.job_title_var.get()

        # Validate input data
        if name and emp_id:
            # Save data to the employee list
            self.employee_list.append((name, emp_id, job_title))
            messagebox.showinfo("Success", "Employee data saved successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields!")

        # Clear entry fields
        self.name_entry.delete(0, tk.END)
        self.emp_id_entry.delete(0, tk.END)

class DisplayEmployeeWindow:
    def __init__(self, master, employee_list):
        self.master = master
        self.master.title("Display Employee")
        self.employee_list = employee_list

        # Label and entry field for employee ID
        self.emp_id_label = tk.Label(master, text="Employee ID:")
        self.emp_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.emp_id_entry = tk.Entry(master)
        self.emp_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to display employee information
        self.display_button = tk.Button(master, text="Display", command=self.display_employee_info)
        self.display_button.grid(row=1, columnspan=2, padx=10, pady=5)

    def display_employee_info(self):
        # Retrieve employee ID from entry field
        emp_id = self.emp_id_entry.get()

        # Search for employee in the employee list
        found_employee = None
        for employee in self.employee_list:
            if employee[1] == emp_id:
                found_employee = employee
                break

        if found_employee:
            # Display employee information
            info_str = f"Name: {found_employee[0]}\nEmployee ID: {found_employee[1]}\nJob Title: {found_employee[2]}"
            messagebox.showinfo("Employee Information", info_str)
        else:
            messagebox.showerror("Error", "Employee ID not found")

class EmployeeWindow:
    def __init__(self, master, employee_list):
        self.master = master
        self.master.title("Add Employee")
        self.employee_list = employee_list

        # Labels and entry fields for attributes
        #Lable name
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        #Lable Employee ID
        self.emp_id_label = tk.Label(master, text="Employee ID:")
        self.emp_id_label.grid(row=1, column=0, padx=10, pady=5)
        self.emp_id_entry = tk.Entry(master)
        self.emp_id_entry.grid(row=1, column=1, padx=10, pady=5)
        #Lable Job Title with options of Manager or Salesperson
        self.job_title_label = tk.Label(master, text="Job Title:")
        self.job_title_label.grid(row=2, column=0, padx=10, pady=5)
        self.job_title_var = tk.StringVar(master)
        self.job_title_var.set("Manager")  # Default job title
        self.job_title_optionmenu = tk.OptionMenu(master, self.job_title_var, "Manager", "Salesperson")
        self.job_title_optionmenu.grid(row=2, column=1, padx=10, pady=5)

        # Button to save employee data
        self.save_button = tk.Button(master, text="Save", command=self.save_employee)
        self.save_button.grid(row=3, columnspan=2, padx=10, pady=5)

    def save_employee(self):
        # Retrieve data from entry fields
        name = self.name_entry.get()
        emp_id = self.emp_id_entry.get()
        job_title = self.job_title_var.get()

        # Validate input data
        if name and emp_id:
            # Save data to the employee list
            self.employee_list.append((name, emp_id, job_title))
            messagebox.showinfo("Success", "Employee data saved successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields!")

        # Clear entry fields
        self.name_entry.delete(0, tk.END)
        self.emp_id_entry.delete(0, tk.END)

class DisplayEmployeeWindow:
    def __init__(self, master, employee_list):
        self.master = master
        self.master.title("Display Employee")
        self.employee_list = employee_list

        # Label and entry field for employee ID
        self.emp_id_label = tk.Label(master, text="Employee ID:")
        self.emp_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.emp_id_entry = tk.Entry(master)
        self.emp_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to display employee information
        self.display_button = tk.Button(master, text="Display", command=self.display_employee_info)
        self.display_button.grid(row=1, columnspan=2, padx=10, pady=5)

    def display_employee_info(self):
        # Retrieve employee ID from entry field
        emp_id = self.emp_id_entry.get()

        # Search for employee in the employee list
        found_employee = None
        for employee in self.employee_list:
            if employee[1] == emp_id:
                found_employee = employee
                break
    #if statment for displying
        if found_employee:
            # Display employee information
            info_str = f"Name: {found_employee[0]}\nEmployee ID: {found_employee[1]}\nJob Title: {found_employee[2]}"
            messagebox.showinfo("Employee Information", info_str)
        else: #error handling
            messagebox.showerror("Error", "Employee ID not found")


class ClientWindow:
    def __init__(self, master, client_data):
        self.master = master
        self.master.title("Add Client")
        self.client_data = client_data

        # Labels and entry fields for client attributes
        # Label for input of Client ID
        self.client_id_label = tk.Label(master, text="Client ID:")
        self.client_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.client_id_entry = tk.Entry(master)
        self.client_id_entry.grid(row=0, column=1, padx=10, pady=5)
        # Label for input of Name
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        # Label for input of Address
        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=2, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=2, column=1, padx=10, pady=5)
        # Label for input of Phone Number
        self.phone_number_label = tk.Label(master, text="Phone Number:")
        self.phone_number_label.grid(row=3, column=0, padx=10, pady=5)
        self.phone_number_entry = tk.Entry(master)
        self.phone_number_entry.grid(row=3, column=1, padx=10, pady=5)
        # Label for input of Budget
        self.budget_label = tk.Label(master, text="Budget:")
        self.budget_label.grid(row=4, column=0, padx=10, pady=5)
        self.budget_entry = tk.Entry(master)
        self.budget_entry.grid(row=4, column=1, padx=10, pady=5)
        # Label for input of Event Type with four options
        # Options for event types
        self.event_type_label = tk.Label(master, text="Event Type:")
        self.event_type_label.grid(row=5, column=0, padx=10, pady=5)
        self.event_type_var = tk.StringVar(master)
        self.event_type_var.set("Wedding")  # Default event type
        self.event_type_optionmenu = tk.OptionMenu(master, self.event_type_var, "Wedding", "Birthday", "Themed Party", "Graduation")
        self.event_type_optionmenu.grid(row=5, column=1, padx=10, pady=5)

        #inputs for he actual event
        # Label for input of Date of the eent wanted
        self.date_label = tk.Label(master, text="Date:")
        self.date_label.grid(row=6, column=0, padx=10, pady=5)
        self.date_entry = tk.Entry(master)
        self.date_entry.grid(row=6, column=1, padx=10, pady=5)
        # Label for input of Tiem of the event
        self.time_label = tk.Label(master, text="Time:")
        self.time_label.grid(row=7, column=0, padx=10, pady=5)
        self.time_entry = tk.Entry(master)
        self.time_entry.grid(row=7, column=1, padx=10, pady=5)

        #Label for input of Venue: 3 Options for venue
        self.venue_label = tk.Label(master, text="Venue:")
        self.venue_label.grid(row=8, column=0, padx=10, pady=5)
        self.venue_var = tk.StringVar(master)
        self.venue_var.set("Hotel")  # Default venue
        self.venue_optionmenu = tk.OptionMenu(master, self.venue_var, "Hotel", "Convention Hall", "Outdoor Space")
        self.venue_optionmenu.grid(row=8, column=1, padx=10, pady=5)

        # Label and entry field for event ID
        self.event_id_label = tk.Label(master, text="Event ID:")
        self.event_id_label.grid(row=9, column=0, padx=10, pady=5)
        self.event_id_entry = tk.Entry(master)
        self.event_id_entry.grid(row=9, column=1, padx=10, pady=5)

        # Button to save client data
        self.save_button = tk.Button(master, text="Save", command=self.save_client)
        self.save_button.grid(row=10, columnspan=2, padx=10, pady=5)
    def save_client(self):
        # Retrieve data from entry fields
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        phone_number = self.phone_number_entry.get()
        budget = self.budget_entry.get()
        event_type = self.event_type_var.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        venue = self.venue_var.get()
        event_id = self.event_id_entry.get()

        # Validate input data
        if client_id and name and address and phone_number and budget and event_type and date and time and venue and event_id:
            # Save data to the client data dictionary
            self.client_data[event_id] = {
                "Client ID": client_id,
                "Name": name,
                "Address": address,
                "Phone Number": phone_number,
                "Budget": budget,
                "Event Type": event_type,
                "Date": date,
                "Time": time,
                "Venue": venue
            }
            messagebox.showinfo("Success", "Client data saved successfully!")
        else: #error handling
            messagebox.showerror("Error", "Please fill in all fields!")

        # Clear entry fields
        self.client_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)
        self.budget_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.event_id_entry.delete(0, tk.END)

class DisplayClientWindow:
    def __init__(self, master, client_data):
        self.master = master
        self.master.title("Display Client")
        self.master.geometry("300x100")
        self.client_data = client_data

        # Label and entry field for event ID
        self.event_id_label = tk.Label(master, text="Event ID:")
        self.event_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.event_id_entry = tk.Entry(master)
        self.event_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to display client information
        self.display_button = tk.Button(master, text="Display", command=self.display_client_info)
        self.display_button.grid(row=1, columnspan=2, padx=10, pady=5)

    def display_client_info(self):
        # Retrieve event ID from entry field
        event_id = self.event_id_entry.get()

        # Check if the event ID exists in the client data
        if event_id in self.client_data:
            # Retrieve client information associated with the event ID
            client_info = self.client_data[event_id]

            # Display client information
            info_str = "\n".join([f"{key}: {value}" for key, value in client_info.items()])
            messagebox.showinfo("Client Information", info_str)
        else: #error handling
            # Display error message if event ID is not found
            messagebox.showerror("Error", "Event ID not found")


class GuestWindow:
    def __init__(self, master, client_data):
        self.master = master
        self.master.title("Add Guest")
        self.client_data = client_data

        # Labels and entry fields for guest attributes
        # Label for name input form guest
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        # Label for Address input form guest
        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=1, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=1, column=1, padx=10, pady=5)
        # Label for Phone Number form guest
        self.phone_number_label = tk.Label(master, text="Phone Number:")
        self.phone_number_label.grid(row=2, column=0, padx=10, pady=5)
        self.phone_number_entry = tk.Entry(master)
        self.phone_number_entry.grid(row=2, column=1, padx=10, pady=5)
        # Label for email input form guest
        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=3, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)
        # Label for event ID input form guest to associate
        # Dropdown menu to select the event
        self.event_label = tk.Label(master, text="Event: ")
        self.event_label.grid(row=4, column=0, padx=10, pady=5)
        self.event_var = tk.StringVar(master)

        # Populate event options if client data is available
        #handling if there is no event of such type
        self.event_options = list(client_data.keys()) if client_data else ["No Events Available"]
        self.event_var.set(self.event_options[0])  # Set default event
        self.event_optionmenu = tk.OptionMenu(master, self.event_var, *self.event_options)
        self.event_optionmenu.grid(row=4, column=1, padx=10, pady=5)

        # Button to save guest data
        self.save_button = tk.Button(master, text="Save", command=self.save_guest)
        self.save_button.grid(row=5, columnspan=2, padx=10, pady=5)

    def save_guest(self):
        # Retrieve data from entry fields
        name = self.name_entry.get()
        address = self.address_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()
        event_id = self.event_var.get()

        # Validate input data
        if name and address and phone_number and email:
            # Here you would save the guest data along with the associated event
            messagebox.showinfo("Success", "Guest data saved successfully!")
        else: #error handling
            messagebox.showerror("Error", "Please fill in all fields!")

        # Clear entry fields
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

class DisplayGuestInfoWindow:
    def __init__(self, master, client_data):
        self.master = master
        self.client_data = client_data

        # Label and entry field for guest ID
        self.guest_id_label = tk.Label(master, text="Guest ID:")
        self.guest_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.guest_id_entry = tk.Entry(master)
        self.guest_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to display guest info
        self.display_button = tk.Button(master, text="Display", command=self.display_guest_info)
        self.display_button.grid(row=1, columnspan=2, padx=10, pady=5)

    def display_guest_info(self):
        # Retrieve guest ID from entry field
        guest_id = self.guest_id_entry.get()

        # Check if the guest ID exists in the client data
        if guest_id in self.client_data:
            # Retrieve guest information associated with the guest ID
            guest_info = self.client_data[guest_id]

            # Display guest information
            info_str = "\n".join([f"{key}: {value}" for key, value in guest_info.items()])
            messagebox.showinfo("Guest Information", info_str)
        else: #error handling
            # Display error message if guest ID is not found
            messagebox.showerror("Error", "Guest ID not found")

class SupplierWindow:
    def __init__(self, master, supplier_list, event_options):
        self.master = master
        self.master.title("Add Supplier")
        self.supplier_list = supplier_list

        # Add attributes for the supplier
        # Label for ID input for supplier
        self.supplier_id_label = tk.Label(master, text="Supplier ID:")
        self.supplier_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.supplier_id_entry = tk.Entry(master)
        self.supplier_id_entry.grid(row=0, column=1, padx=10, pady=5)
        # Label for name input for supplier
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        # Label for the product the supplier will supply
        self.product_label = tk.Label(master, text="Product:")
        self.product_label.grid(row=2, column=0, padx=10, pady=5)
        self.product_entry = tk.Entry(master)
        self.product_entry.grid(row=2, column=1, padx=10, pady=5)
        # Label for number input for supplier
        self.phone_number_label = tk.Label(master, text="Phone Number:")
        self.phone_number_label.grid(row=3, column=0, padx=10, pady=5)
        self.phone_number_entry = tk.Entry(master)
        self.phone_number_entry.grid(row=3, column=1, padx=10, pady=5)
        # Label for email input for supplier
        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=4, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=4, column=1, padx=10, pady=5)
        # Label for the event the suppler will supply to
        self.event_label = tk.Label(master, text="Event:")
        self.event_label.grid(row=5, column=0, padx=10, pady=5)
        self.event_var = tk.StringVar(master) #handle non existnt eent id
        self.event_var.set(event_options[0] if event_options else "No Events Available")
        self.event_optionmenu = tk.OptionMenu(master, self.event_var, *event_options)
        self.event_optionmenu.grid(row=5, column=1, padx=10, pady=5)

        # Button to save supplier data
        self.save_button = tk.Button(master, text="Save", command=self.save_supplier)
        self.save_button.grid(row=6, columnspan=2, padx=10, pady=5)

    def save_supplier(self):
        # Retrieve data from entry fields
        supplier_id = self.supplier_id_entry.get()
        name = self.name_entry.get()
        product = self.product_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()
        event_id = self.event_var.get()

        # Validate input data
        if supplier_id and name and product and phone_number and email:
            # Here you can handle the supplier data as needed
            # Assuming you add the supplier to supplier_list
            self.supplier_list.append((supplier_id, name, product, phone_number, email, event_id))
            messagebox.showinfo("Success", "Supplier data saved successfully!")
        else:   #error handling
            messagebox.showerror("Error", "Please fill in all fields!")

        # Clear entry fields
        self.supplier_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.product_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

# New class for displaying supplier information
class DisplaySupplierInfoWindow:
    def __init__(self, master, supplier_list):
        self.master = master
        self.master.title("Display Supplier Info")
        self.supplier_list = supplier_list

        # Label and entry field for supplier ID
        self.supplier_id_label = tk.Label(master, text="Supplier ID:")
        self.supplier_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.supplier_id_entry = tk.Entry(master)
        self.supplier_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to display supplier information
        self.display_button = tk.Button(master, text="Display", command=self.display_supplier_info)
        self.display_button.grid(row=1, columnspan=2, padx=10, pady=5)

    def display_supplier_info(self):
        # Retrieve supplier ID from entry field
        supplier_id = self.supplier_id_entry.get()

        # Search for supplier in the supplier list
        found_supplier = None
        for supplier in self.supplier_list:
            if supplier[0] == supplier_id:
                found_supplier = supplier
                break

        if found_supplier:
            # Display supplier information
            info_str = f"Name: {found_supplier[1]}\nProduct: {found_supplier[2]}\nPhone Number: {found_supplier[3]}\nEmail: {found_supplier[4]}"
            messagebox.showinfo("Supplier Information", info_str)
        else:  #error handling
            messagebox.showerror("Error", "Supplier ID not found")


class VenueWindow:
    def __init__(self, master, venue_list):
        self.master = master
        self.master.title("Add Venue")
        self.venue_list = venue_list

        # Labels and entry fields for venue attributes
        self.venue_id_label = tk.Label(master, text="Venue ID:")
        self.venue_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.venue_id_entry = tk.Entry(master)
        self.venue_id_entry.grid(row=0, column=1, padx=10, pady=5)
#input for name and every other "text="
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        #Label for adress where the  venue willl take place
        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=2, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=2, column=1, padx=10, pady=5)
        #Label for the contant info of the  venue
        self.contact_label = tk.Label(master, text="Contact:")
        self.contact_label.grid(row=3, column=0, padx=10, pady=5)
        self.contact_entry = tk.Entry(master)
        self.contact_entry.grid(row=3, column=1, padx=10, pady=5)
        #Label for the minimum amount of people who can attend/fit
        self.min_guests_label = tk.Label(master, text="Min Guests:")
        self.min_guests_label.grid(row=4, column=0, padx=10, pady=5)
        self.min_guests_entry = tk.Entry(master)
        self.min_guests_entry.grid(row=4, column=1, padx=10, pady=5)
        #Label for the maximum amount of people who can attend/fit
        self.max_guests_label = tk.Label(master, text="Max Guests:")
        self.max_guests_label.grid(row=5, column=0, padx=10, pady=5)
        self.max_guests_entry = tk.Entry(master)
        self.max_guests_entry.grid(row=5, column=1, padx=10, pady=5)

        # Button to save venue data
        self.save_button = tk.Button(master, text="Save", command=self.save_venue)
        self.save_button.grid(row=6, columnspan=2, padx=10, pady=5)

    def save_venue(self):
        # Retrieve data from entry fields
        venue_id = self.venue_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        # Validate input data
        if venue_id and name and address and contact and min_guests and max_guests:
            # Here you can handle the venue data as needed
            # Assuming you add the venue to venue_list
            self.venue_list.append((venue_id, name, address, contact, min_guests, max_guests))
            messagebox.showinfo("Success", "Venue data saved successfully!")
        else:  #error handling
            messagebox.showerror("Error", "Please fill in all fields!")

        # Clear entry fields
        self.venue_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.min_guests_entry.delete(0, tk.END)
        self.max_guests_entry.delete(0, tk.END)

class DisplayVenueInfoWindow:
    def __init__(self, master, venue_list):
        self.master = master
        self.master.title("Display Venue Info")
        self.venue_list = venue_list

        # Label and entry field for venue ID
        self.venue_id_label = tk.Label(master, text="Venue ID:")
        self.venue_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.venue_id_entry = tk.Entry(master)
        self.venue_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to display venue information
        self.display_button = tk.Button(master, text="Display", command=self.display_venue_info)
        self.display_button.grid(row=1, columnspan=2, padx=10, pady=5)

    def display_venue_info(self):
        # Retrieve venue ID from entry field
        venue_id = self.venue_id_entry.get()

        # Search for venue in the venue list
        found_venue = None
        for venue in self.venue_list:
            if venue[0] == venue_id:
                found_venue = venue
                break

        if found_venue:
            # Display venue information
            info_str = f"Name: {found_venue[1]}\nAddress: {found_venue[2]}\nContact: {found_venue[3]}\nMin Guests: {found_venue[4]}\nMax Guests: {found_venue[5]}"
            messagebox.showinfo("Venue Information", info_str)
        else:       #error handling
            messagebox.showerror("Error", "Venue ID not found")

class ModifyEmployeeWindow:
    def __init__(self, master, employee_list, status_bar):
        ###


        self.master = master
        self.master.title("Modify Employee")
        self.employee_list = employee_list
        self.status_bar = status_bar
        # Widgets to input and display employee ID
        self.emp_id_label = tk.Label(master, text="Employee ID:")
        self.emp_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.emp_id_entry = tk.Entry(master)
        self.emp_id_entry.grid(row=0, column=1, padx=10, pady=5)
        # Button to load employee data
        self.load_button = tk.Button(master, text="Load", command=self.load_employee)
        self.load_button.grid(row=1, column=0, columnspan=2)
        # Widgets for modifying employee data (hidden until load is successful)
        self.name_label = tk.Label(master, text="Name:")
        self.name_entry = tk.Entry(master)
        self.job_title_label = tk.Label(master, text="Job Title:")
        self.job_title_entry = tk.Entry(master)
        # Button to save modifications
        self.save_button = tk.Button(master, text="Save", command=self.save_employee)

    def load_employee(self):
        emp_id = self.emp_id_entry.get()
        for employee in self.employee_list:
            if employee[1] == emp_id:
                self.name_entry.insert(0, employee[0])
                self.job_title_entry.insert(0, employee[2])
                self.display_employee_fields()
                return
        messagebox.showerror("Error", "Employee ID not found")
    def display_employee_fields(self):
        self.name_label.grid(row=2, column=0)
        self.name_entry.grid(row=2, column=1)
        self.job_title_label.grid(row=3, column=0)
        self.job_title_entry.grid(row=3, column=1)
        self.save_button.grid(row=4, columnspan=2)
    def save_employee(self):
        emp_id = self.emp_id_entry.get()
        new_name = self.name_entry.get()
        new_job_title = self.job_title_entry.get()

        if not new_name or not new_job_title:
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        # Find and update the employee
        for index, employee in enumerate(self.employee_list):
            if employee[1] == emp_id:
                # Update the employee details
                updated_employee = (new_name, emp_id, new_job_title)
                self.employee_list[index] = updated_employee
                messagebox.showinfo("Success", "Employee updated successfully!")
                self.status_bar.config(text="Updated employee details successfully.")
                self.master.destroy()  # Optionally close the window
                return

        # If not found, display an error message
        messagebox.showerror("Error", "Employee not found. Please reload and try again.")


class ModifyClientWindow:
    def __init__(self, master, client_data, status_bar):
        self.master = master
        self.master.title("Modify Client and Event")
        self.client_data = client_data
        self.status_bar = status_bar

        # Widgets to input and display client ID
        self.client_id_label = tk.Label(master, text="Client ID:")
        self.client_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.client_id_entry = tk.Entry(master)
        self.client_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to load client data
        self.load_button = tk.Button(master, text="Load", command=self.load_client)
        self.load_button.grid(row=1, column=0, columnspan=2)

        # Widgets for modifying client data (hidden until load is successful)
        self.name_label = tk.Label(master, text="Name:")
        self.name_entry = tk.Entry(master)
        self.phone_label = tk.Label(master, text="Phone Number:")
        self.phone_entry = tk.Entry(master)
        self.budget_label = tk.Label(master, text="Budget:")
        self.budget_entry = tk.Entry(master)

        # Button to save modifications
        self.save_button = tk.Button(master, text="Save", command=self.save_client)

    def load_client(self):
        client_id = self.client_id_entry.get()
        client = self.client_data.get(client_id)
        if client:
            self.name_entry.insert(0, client['Name'])
            self.phone_entry.insert(0, client['Phone Number'])
            self.budget_entry.insert(0, client['Budget'])
            self.display_client_fields()
        else:   #error handling
            messagebox.showerror("Error", "Client ID not found")

    def display_client_fields(self):
        self.name_label.grid(row=2, column=0)
        self.name_entry.grid(row=2, column=1)
        self.phone_label.grid(row=3, column=0)
        self.phone_entry.grid(row=3, column=1)
        self.budget_label.grid(row=4, column=0)
        self.budget_entry.grid(row=4, column=1)
        self.save_button.grid(row=5, columnspan=2)

    def save_client(self):
        client_id = self.client_id_entry.get()
        new_name = self.name_entry.get()
        new_phone = self.phone_entry.get()
        new_budget = self.budget_entry.get()

        if not new_name or not new_phone or not new_budget:
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        if client_id in self.client_data:
            self.client_data[client_id] = {
                'Name': new_name,
                'Phone Number': new_phone,
                'Budget': new_budget
            }
            messagebox.showinfo("Success", "Client updated successfully!")
            self.status_bar.config(text="Updated client details successfully.")
        else:  #error handling
            messagebox.showerror("Error", "Client not found. Please reload and try again.")

class ModifySupplierWindow:
    def __init__(self, master, supplier_list, status_bar):
        self.master = master
        self.master.title("Modify Supplier")
        self.supplier_list = supplier_list
        self.status_bar = status_bar
        #lables that can be modified
        self.supplier_id_label = tk.Label(master, text="Supplier ID:")
        self.supplier_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.supplier_id_entry = tk.Entry(master)
        self.supplier_id_entry.grid(row=0, column=1, padx=10, pady=5)
        #lables that can be modified
        self.load_button = tk.Button(master, text="Load", command=self.load_supplier)
        self.load_button.grid(row=1, columnspan=2)
        #lables that can be modified
        self.name_label = tk.Label(master, text="Name:")
        self.name_entry = tk.Entry(master)
        self.product_label = tk.Label(master, text="Product:")
        self.product_entry = tk.Entry(master)

        self.save_button = tk.Button(master, text="Save", command=self.save_supplier)
    def load_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        for supplier in self.supplier_list:
            if supplier[0] == supplier_id:
                self.name_entry.insert(0, supplier[1])
                self.product_entry.insert(0, supplier[2])
                self.display_supplier_fields()
                return #error handling
        messagebox.showerror("Error", "Supplier ID not found")
    def display_supplier_fields(self):
        self.name_label.grid(row=2, column=0)
        self.name_entry.grid(row=2, column=1)
        self.product_label.grid(row=3, column=0)
        self.product_entry.grid(row=3, column=1)
        self.save_button.grid(row=4, columnspan=2)
    def save_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        new_name = self.name_entry.get()
        new_product = self.product_entry.get()

        if not new_name or not new_product:
            messagebox.showerror("Error", "All fields must be filled out.")
            return
        found = False
        for index, supplier in enumerate(self.supplier_list):
            if supplier[0] == supplier_id:
                self.supplier_list[index] = (supplier_id, new_name, new_product)
                messagebox.showinfo("Success", "Supplier updated successfully!")
                self.status_bar.config(text="Updated supplier details successfully.")
                found = True
                break
        if not found: #error handling
            messagebox.showerror("Error", "Supplier not found. Please reload and try again.")


class ModifyGuestWindow:
    def __init__(self, master, guest_data, status_bar):
        self.master = master
        self.master.title("Modify Guest")
        self.guest_data = guest_data
        self.status_bar = status_bar
        #lables that can be modified
        self.guest_id_label = tk.Label(master, text="Guest ID:")
        self.guest_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.guest_id_entry = tk.Entry(master)
        self.guest_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.load_button = tk.Button(master, text="Load", command=self.load_guest)
        self.load_button.grid(row=1, columnspan=2)
        #lables that can be modified
        self.name_label = tk.Label(master, text="Name:")
        self.name_entry = tk.Entry(master)
        self.address_label = tk.Label(master, text="Address:")
        self.address_entry = tk.Entry(master)
        self.contact_label = tk.Label(master, text="Contact Details:")
        self.contact_entry = tk.Entry(master)

        self.save_button = tk.Button(master, text="Save", command=self.save_guest)
    def load_guest(self):
        guest_id = self.guest_id_entry.get()
        guest = self.guest_data.get(guest_id)
        if guest:
            self.name_entry.insert(0, guest['Name'])
            self.address_entry.insert(0, guest['Address'])
            self.contact_entry.insert(0, guest['Contact Details'])
            self.display_guest_fields()
        else: #error handling
            messagebox.showerror("Error", "Guest ID not found")
    def display_guest_fields(self):
        #position in the webpage
        self.name_label.grid(row=2, column=0)
        self.name_entry.grid(row=2, column=1)
        self.address_label.grid(row=3, column=0)
        self.address_entry.grid(row=3, column=1)
        self.contact_label.grid(row=4, column=0)
        self.contact_entry.grid(row=4, column=1)
        self.save_button.grid(row=5, columnspan=2)
    def save_guest(self):
        guest_id = self.guest_id_entry.get()
        new_name = self.name_entry.get()
        new_address = self.address_entry.get()
        new_contact = self.contact_entry.get()
        if not new_name or not new_address or not new_contact:
            messagebox.showerror("Error", "All fields must be filled out.")
            return
        if guest_id in self.guest_data:
            self.guest_data[guest_id] = {
                'Name': new_name,
                'Address': new_address,
                'Contact Details': new_contact
            }
            messagebox.showinfo("Success", "Guest updated successfully!")
            self.status_bar.config(text="Updated guest details successfully.")
        else: #error handling
            messagebox.showerror("Error", "Guest not found. Please reload and try again.")


class ModifyVenueWindow:
    def __init__(self, master, venue_list, status_bar):
        self.master = master
        self.master.title("Modify Venue")
        self.venue_list = venue_list
        self.status_bar = status_bar

        self.venue_id_label = tk.Label(master, text="Venue ID:")
        self.venue_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.venue_id_entry = tk.Entry(master)
        self.venue_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.load_button = tk.Button(master, text="Load", command=self.load_venue)
        self.load_button.grid(row=1, columnspan=2)

        self.name_label = tk.Label(master, text="Name:")        #lables that can be modified
        self.name_entry = tk.Entry(master)
        self.address_label = tk.Label(master, text="Address:")        #lables that can be modified
        self.address_entry = tk.Entry(master)
        self.contact_label = tk.Label(master, text="Contact:")        #lables that can be modified
        self.contact_entry = tk.Entry(master)
        self.min_guests_label = tk.Label(master, text="Min Guests:")        #lables that can be modified
        self.min_guests_entry = tk.Entry(master)
        self.max_guests_label = tk.Label(master, text="Max Guests:")        #lables that can be modified
        self.max_guests_entry = tk.Entry(master)

        self.save_button = tk.Button(master, text="Save", command=self.save_venue)
    def load_venue(self):
        venue_id = self.venue_id_entry.get()
        for venue in self.venue_list:
            if venue[0] == venue_id:
                self.name_entry.insert(0, venue[1])
                self.address_entry.insert(0, venue[2])
                self.contact_entry.insert(0, venue[3])
                self.min_guests_entry.insert(0, venue[4])
                self.max_guests_entry.insert(0, venue[5])
                self.display_venue_fields()
                return
        messagebox.showerror("Error", "Venue ID not found")
    def display_venue_fields(self):
        #positino for the button on page
        self.name_label.grid(row=2, column=0)
        self.name_entry.grid(row=2, column=1)
        self.address_label.grid(row=3, column=0)
        self.address_entry.grid(row=3, column=1)
        self.contact_label.grid(row=4, column=0)
        self.contact_entry.grid(row=4, column=1)
        self.min_guests_label.grid(row=5, column=0)
        self.min_guests_entry.grid(row=5, column=1)
        self.max_guests_label.grid(row=6, column=0)
        self.max_guests_entry.grid(row=6, column=1)
        self.save_button.grid(row=7, columnspan=2)
    def save_venue(self):
        venue_id = self.venue_id_entry.get()
        new_name = self.name_entry.get()
        new_address = self.address_entry.get()
        new_contact = self.contact_entry.get()
        new_min_guests = self.min_guests_entry.get()
        new_max_guests = self.max_guests_entry.get()
        if not new_name or not new_address or not new_contact or not new_min_guests or not new_max_guests:
            messagebox.showerror("Error", "All fields must be filled out.")
            return
        for index, venue in enumerate(self.venue_list):
            if venue[0] == venue_id:
                updated_venue = (venue_id, new_name, new_address, new_contact, new_min_guests, new_max_guests)
                self.venue_list[index] = updated_venue
                messagebox.showinfo("Success", "Venue updated successfully!")
                self.status_bar.config(text="Updated venue details successfully.")
                break
        else: #error handling
            messagebox.showerror("Error", "Venue not found. Please reload and try again.")


class DeleteEmployeeWindow:
    def __init__(self, master, employee_list, status_bar):
        self.master = master
        self.master.title("Delete Employee")
        self.employee_list = employee_list
        self.status_bar = status_bar

        # Label and entry field for employee ID
        self.emp_id_label = tk.Label(master, text="Employee ID:")
        self.emp_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.emp_id_entry = tk.Entry(master)
        self.emp_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to delete employee
        self.delete_button = tk.Button(master, text="Delete", command=self.delete_employee)
        self.delete_button.grid(row=1, columnspan=2, padx=10, pady=5)
    def delete_employee(self):
        emp_id = self.emp_id_entry.get()
        # Find and delete the employee by ID
        for i, employee in enumerate(self.employee_list):
            if employee[1] == emp_id:
                self.employee_list.pop(i)
                messagebox.showinfo("Success", "Employee deleted successfully!")
                self.status_bar.config(text="Employee deleted successfully!")
                return

        messagebox.showerror("Error", "Employee ID not found") #error handling
        self.status_bar.config(text="Employee ID not found")



class DeleteClientWindow:
    def __init__(self, master, client_data, status_bar):
        self.master = master
        self.master.title("Delete Client")
        self.client_data = client_data
        self.status_bar = status_bar
        # Label of Client ID
        self.client_id_label = tk.Label(master, text="Client ID:")
        self.client_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.client_id_entry = tk.Entry(master)
        self.client_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.delete_button = tk.Button(master, text="Delete", command=self.delete_client)
        self.delete_button.grid(row=1, columnspan=2, padx=10, pady=5)
    def delete_client(self):
        client_id = self.client_id_entry.get()
        if client_id in self.client_data:
            del self.client_data[client_id]
            #messege that will pop when saved info
            messagebox.showinfo("Success", "Client deleted successfully!")
            self.status_bar.config(text="Client deleted successfully!")
        else:   #error handling
            messagebox.showerror("Error", "Client ID not found")
            self.status_bar.config(text="Client ID not found")

class DeleteGuestWindow:
    def __init__(self, master, guest_data, status_bar):
        self.master = master
        self.master.title("Delete Guest")
        self.guest_data = guest_data
        self.status_bar = status_bar

        self.guest_id_label = tk.Label(master, text="Guest ID:")
        self.guest_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.guest_id_entry = tk.Entry(master)
        self.guest_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.delete_button = tk.Button(master, text="Delete", command=self.delete_guest)
        self.delete_button.grid(row=1, columnspan=2, padx=10, pady=5)
    def delete_guest(self):
        guest_id = self.guest_id_entry.get()
        if guest_id in self.guest_data:
            del self.guest_data[guest_id]
            messagebox.showinfo("Success", "Guest deleted successfully!")
            self.status_bar.config(text="Guest deleted successfully!")
        else:   #error handling
            messagebox.showerror("Error", "Guest ID not found")
            self.status_bar.config(text="Guest ID not found")


class DeleteSupplierWindow:
    def __init__(self, master, supplier_list, status_bar):
        self.master = master
        self.master.title("Delete Supplier")
        self.supplier_list = supplier_list
        self.status_bar = status_bar

        self.supplier_id_label = tk.Label(master, text="Supplier ID:")
        self.supplier_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.supplier_id_entry = tk.Entry(master)
        self.supplier_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.delete_button = tk.Button(master, text="Delete", command=self.delete_supplier)
        self.delete_button.grid(row=1, columnspan=2, padx=10, pady=5)
    def delete_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        # Iterate through the list to find and delete the supplier by ID
        for i, supplier in enumerate(self.supplier_list):
            if supplier[0] == supplier_id:  # Assuming the supplier ID is the first item in the tuple
                del self.supplier_list[i]
                messagebox.showinfo("Success", "Supplier deleted successfully!")
                self.status_bar.config(text="Supplier deleted successfully!")
                return

        messagebox.showerror("Error", "Supplier ID not found") #error handling
        self.status_bar.config(text="Supplier ID not found")

class DeleteVenueWindow:
    def __init__(self, master, venue_list, status_bar):
        self.master = master
        self.master.title("Delete Venue")
        self.venue_list = venue_list
        self.status_bar = status_bar

        # Label and entry field for venue ID
        # Label of Venue ID
        self.venue_id_label = tk.Label(master, text="Venue ID:")
        self.venue_id_label.grid(row=0, column=0, padx=10, pady=5)
        self.venue_id_entry = tk.Entry(master)
        self.venue_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to delete venue
        self.delete_button = tk.Button(master, text="Delete", command=self.delete_venue)
        self.delete_button.grid(row=1, columnspan=2, padx=10, pady=5)

    def delete_venue(self):
        venue_id = self.venue_id_entry.get()
        for i, venue in enumerate(self.venue_list):
            if venue[0] == venue_id:
                self.venue_list.pop(i)
                messagebox.showinfo("Success", "Venue deleted successfully!")
                self.status_bar.config(text="Venue deleted successfully!")
                return
        # error handling
        messagebox.showerror("Error", "Venue ID not found")
        self.status_bar.config(text="Venue ID not found")


# Create main window
root = tk.Tk()

#initializing the MainWindow
app = MainWindow(root)

# Runnin the application
root.mainloop()