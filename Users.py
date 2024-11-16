
#Employee
#Admin

from abc import ABC

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
    
class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = None
    
    def view_menu(self, restaurant):
        restaurant.menu.show_menu()
    
    def add_to_cart(self, restaurant, item_name):
        item = restaurant.menu.find_item(item_name)
        if item:
            pass
        else:
            print("Item not found")

    def view_cart(self):
        print(***View Cart***)
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
            print(f"Total Price : {self.cart.total_price}")

 class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity
    def remove(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())     

    def clear(self):
        self.items = {}      


class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        
    
    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)
        
    
    def show_employee_list(self, restaurant):
        restaurant.view_employee()
    
    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)
    
    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)
       

class Restaurant:

    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = FoodItem()

    def add_employee(self, employee):
        self.employee.append(employee)
    
    def view_employee(self):
        print("Employee List Here: ")

        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address, emp.age, emp.designation, emp.salary)

class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)
    
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return item

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Deleted")
        else:
            print("Item not found")
    def show_menu(self):
        print("*******Menu********")
        print(f"Name\tprice\tquantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    


mn = Menu()
item = FoodItem("Pizza", 25.09, 10)
mn.add_menu_item(item)

mn.show_menu()

