import tkinter as tk
from tkinter import messagebox


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Management System")

        # List to store employee data
        self.employee_list = []

        # Buttons for different options
        self.employee_button = tk.Button(master, text="Add Employee", command=self.open_employee_window)
        self.employee_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        # Button to display employee list
        self.display_employee_button = tk.Button(master, text="Display Employees", command=self.display_employees)
        self.display_employee_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Button to add client
        self.client_button = tk.Button(master, text="Add Client", command=self.open_client_window)
        self.client_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

    def open_employee_window(self):
        employee_window = tk.Toplevel(self.master)
        EmployeeWindow(employee_window, self.employee_list)

    def open_client_window(self):
        client_window = tk.Toplevel(self.master)
        ClientWindow(client_window)

    def display_employees(self):
        # Create a window to display employee list
        display_window = tk.Toplevel(self.master)
        EmployeeDisplayWindow(display_window, self.employee_list)


class EmployeeDisplayWindow:
    def __init__(self, master, employee_list):
        self.master = master
        self.master.title("Employee List")
        self.employee_list = employee_list

        # Create a label to display employee list
        self.employee_label = tk.Label(master, text="Employee List", font=("Arial", 14, "bold"))
        self.employee_label.pack()

        # Create a text widget to display employee data
        self.employee_text = tk.Text(master, height=20, width=50)
        self.employee_text.pack(pady=10)

        # Insert employee data into text widget
        self.display_employees()
