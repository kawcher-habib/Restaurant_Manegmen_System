from menu import Menu
class Restaurant:

    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employee.append(employee)
    
    def view_employee(self):
        print("Employee List Here: ")

        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address, emp.age, emp.designation, emp.salary)
