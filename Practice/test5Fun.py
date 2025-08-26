# Default Parameter
def send_message(animal,name="pp"):
    print(f"{animal} named {name}")
send_message("Dog")
send_message(animal="cat",name="max")


# def send_message(message, recipient="Friend"):
#     print(f"Sending '{message}' to {recipient}.")
# send_message("Hi there!")         
# send_message("See you soon!", "John")


def message(*names):
    for name in names:
        print(f"Names are {name}")
message("Alice", "Bob", "Charlie")

def print_p(**arg):
    for key,value in arg.items():
        print(f"{key}: {value}")
print_p(name="David", age=30, city="New York")

# Lambda Function

add=lambda x:x+10
print(add(5))

names = ["alice", "bob", "charlie"]
capital=list(map(lambda name:name.capitalize(),names))
print(f"Capital_names{capital}")


# students = [
#     {"name": "Alice", "age": 25, "score": 90},
#     {"name": "Bob", "age": 22, "score": 85},
#     {"name": "Charlie", "age": 28, "score": 95}
# ]
# sorted_students=sorted(students, key=lambda stu:stu["score"])
# for student in students:
#     print(f"Students age{students}")


def calculate_area(base,height,shape):
  
    if shape == "triangle":
        area = (1/2)*base*height
        return area
    elif shape == "rectriangle":
        area=base*height
        return area
    else:
        return "Error"

base=float(input(print("Put the base: ")))
height=float(input(print("Put the height: ")))
shape = input("Enter the shape (triangle or rectangle): ")
area=calculate_area(base,height,shape)
print("Area is:",area)


for i in range():
    s=''
    for j in range(i):
        s=s+"*"
    print(s)

