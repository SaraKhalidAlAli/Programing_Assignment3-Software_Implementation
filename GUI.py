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
        self.display_employee_button = tk.Button(master, text="Display Employees", command=self.display_employees)
        self.display_employee_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        self.client_button = tk.Button(master, text="Add Client", command=self.open_client_window)
        self.client_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.guest_button = tk.Button(master, text="Add Guest", command=self.open_guest_window)
        self.guest_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.supplier_button = tk.Button(master, text="Add Supplier", command=self.open_supplier_window)
        self.supplier_button.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        # Button to display employee list
        self.display_employee_button = tk.Button(master, text="Display Employees", command=self.display_employees)
        self.display_employee_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        # Status bar
        self.status_bar = tk.Label(master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.grid(row=5, column=0, sticky=tk.W + tk.E)