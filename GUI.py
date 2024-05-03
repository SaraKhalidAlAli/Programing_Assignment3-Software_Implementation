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
