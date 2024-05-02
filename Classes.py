#adding the classes

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
class Event:
class Guest:
class Venue:
class Supplier:
class Caterer: