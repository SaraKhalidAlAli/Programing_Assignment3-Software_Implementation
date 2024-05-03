import tkinter as tk
from tkinter import messagebox
import pickle

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Management System")

        self.employee_list = self.load_data('employees.pkl')
        self.client_data = self.load_data('clients.pkl')
        self.supplier_list = self.load_data('suppliers.pkl')
        self.venue_list = self.load_data('venues.pkl')

        # Buttons for different options
        self.employee_button = tk.Button(master, text="Add Employee", command=self.open_employee_window)
        self.employee_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.display_employee_button = tk.Button(master, text="Display Employees", command=self.open_display_employee_window)
        self.display_employee_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        self.client_button = tk.Button(master, text="Add Client", command=self.open_client_window)
        self.client_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.display_client_button = tk.Button(master, text="Display Client Event Info", command=self.open_display_client_window)
        self.display_client_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.guest_button = tk.Button(master, text="Add Guest", command=self.open_guest_window)
        self.guest_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        self.display_guest_info_button = tk.Button(master, text="Display Guest's Info", command=self.open_display_guest_info_window)
        self.display_guest_info_button.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        self.supplier_button = tk.Button(master, text="Add Supplier", command=self.open_supplier_window)
        self.supplier_button.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        self.display_supplier_info_button = tk.Button(master, text="Display Supplier's Info", command=self.open_display_supplier_info_window)
        self.display_supplier_info_button.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        self.venue_button = tk.Button(master, text="Add Venue", command=self.open_venue_window)
        self.venue_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        self.display_venue_info_button = tk.Button(master, text="Display Venue Info", command=self.open_display_venue_info_window)
        self.display_venue_info_button.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        self.status_bar = tk.Label(master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.grid(row=5, column=0, sticky=tk.W + tk.E)

    def load_data(self, filename):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return []

    def save_data(self, data, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(data, f)
        except pickle.PicklingError:
            messagebox.showerror("Error", "Failed to save data.")

    def open_employee_window(self):
        employee_window = tk.Toplevel(self.master)
        EmployeeWindow(employee_window, self.employee_list, self.save_data)

    def open_display_employee_window(self):
        display_employee_window = tk.Toplevel(self.master)
        DisplayEmployeeWindow(display_employee_window, self.employee_list)

    def open_client_window(self):
        client_window = tk.Toplevel(self.master)
        ClientWindow(client_window, self.client_data, self.save_data)

    def open_display_client_window(self):
        display_client_window = tk.Toplevel(self.master)
        DisplayClientWindow(display_client_window, self.client_data)

    def open_guest_window(self):
        guest_window = tk.Toplevel(self.master)
        GuestWindow(guest_window, self.client_data, self.save_data)

    def open_display_guest_info_window(self):
        display_guest_info_window = tk.Toplevel(self.master)
        DisplayGuestInfoWindow(display_guest_info_window, self.client_data)

    def open_supplier_window(self):
        supplier_window = tk.Toplevel(self.master)
        SupplierWindow(supplier_window, self.supplier_list, ["Event 1", "Event 2"], self.save_data)

    def open_display_supplier_info_window(self):
        display_supplier_info_window = tk.Toplevel(self.master)
        DisplaySupplierInfoWindow(display_supplier_info_window, self.supplier_list)

    def open_venue_window(self):
        venue_window = tk.Toplevel(self.master)
        VenueWindow(venue_window, self.venue_list, self.save_data)

    def open_display_venue_info_window(self):
        display_venue_info_window = tk.Toplevel(self.master)
        DisplayVenueInfoWindow(display_venue_info_window, self.venue_list)


class EmployeeWindow:
    def __init__(self, master, employee_list, save_data):
        self.master = master
        self.master.title("Add Employee")
        self.employee_list = employee_list
        self.save_data = save_data  # Save function passed from MainWindow

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
        name = self.name_entry.get()
        try:
            emp_id = int(self.emp_id_entry.get())  # Validate emp_id as integer
            if name and emp_id:
                self.employee_list.append((name, emp_id, self.job_title_var.get()))
                self.save_data(self.employee_list, 'employees.pkl')  # Save the updated list
                messagebox.showinfo("Success", "Employee data saved successfully!")
                self.name_entry.delete(0, tk.END)
                self.emp_id_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please fill in all fields!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Employee ID. Please enter a valid integer.")

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
        emp_id = self.emp_id_entry.get()
        try:
            emp_id = int(emp_id)
            found_employee = next((emp for emp in self.employee_list if emp[1] == emp_id), None)
            if found_employee:
                info_str = f"Name: {found_employee[0]}\nEmployee ID: {found_employee[1]}\nJob Title: {found_employee[2]}"
                messagebox.showinfo("Employee Information", info_str)
            else:
                messagebox.showerror("Error", "Employee ID not found")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Employee ID. Please enter a valid integer.")
