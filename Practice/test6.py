# num1 = int(input("Enter numerator: "))
# num2 = int(input("Enter denominator: "))
# try:
#     result=num1/num2
# except Exception as e:
#     print("Exception occured :",e)
#     result=None
# print("Divisior is ",result)


# class AdultException(Exception):
#     pass


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_minor_age(self):
#         if (self.age) >= 18:
#             raise AdultException
#         else:
#             return self.age

#     def display(self):
#         try:
#             print(f"age {self.get_minor_age()}")
#         except AdultException:
#             print("Adult")
#         finally:
#             print(f"self :{self.name}")

# Person("Pk",20).display()


# class Car:
#     num_wheels=4

#     def __init__(self,color,model):
#         self.model=model
#         self.color=color
#         self.is_running = False
#     def start_enginee(self):
#         if not self.is_running:
#             self.is_running=True
#             print(f"{self.color} and {self.model} enginee started")
#         else:
#             print(f"{self.color} and {self.model} enginee already started")
#     def stop_enginee(self):
#         if self.is_running:
#             self.is_running = False
#             print(f"The {self.color} and {self.model} enginee stopped ")
#         else:
#             print(f"The {self.color} and {self.model} enginee already stopped ")

# my_car = Car("Camry","blue")
# your_car = Car( "Civic","red")
# print(f"My car is {my_car.model}")
# my_car.start_enginee()
# print(f"Is my car running? {my_car.is_running}")


class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(f"id: {self.id} and name {self.name}")

emp = Employee(1, "coder")
emp.display()
del emp.id

try:
    print(emp.id)
except AttributeError:
    print("emp.id is not find ")

print("Program finished")


