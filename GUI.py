import tkinter as tk
from tkinter import messagebox


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Management System")

        # List to store employee data
        self.employee_list = []
        # Dictionary to store client data
        self.client_data = {}
        # List to store supplier data
        self.supplier_list = []
        # List to store supplier data
        self.venue_list = []

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

        # Add a button for adding venues in MainWindow
        self.venue_button = tk.Button(master, text="Add Venue", command=self.open_venue_window)
        self.venue_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        # Add a button for displaying venue information in MainWindow
        self.display_venue_info_button = tk.Button(master, text="Display Venue Info", command=self.open_display_venue_info_window)
        self.display_venue_info_button.grid(row=4, column=1, padx=10, pady=5, sticky="ew")