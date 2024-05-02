import tkinter as tk
from tkinter import messagebox

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Management System")

        # Buttons for different options
        self.employee_button = tk.Button(master, text="Employees", command=self.open_employee_window)
        self.employee_button.grid(row=0, column=0, padx=10, pady=5)
