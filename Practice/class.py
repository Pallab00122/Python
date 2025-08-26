class Father:
    def skills(self):
        print("AAA")
class Mother:
    def skills(self):
        print("BB")
class child(Father,Mother):
    def skil(self):
        Father.skills(self)
        Mother.skills(self)
c=child()
c.skil()
# =====-------------=====
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")
s=Student("Rahul",20,80)
s.display()

class BankAccount:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self.balance +=amount
        print("Deposit : ",amount)
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance -=amount
            print("Withdraw : ",amount)
        else:
            print("Insufficient balance ")
    def show_balance(self):
        print("Balance:", self.balance)

acc=BankAccount()
acc.deposit(1000)
acc.withdraw(500)
acc.show_balance()

# =====-----------======

# ======---------========Overriding
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.employee_id}, Salary: {self.salary}")

e = Employee("Amit", 30, "E123", 50000)
e.show_details()

