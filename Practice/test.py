x = "ab"
def func():
    global x
    x = "cd"
func()
print("Python "+x)

x = 1
print(f'The price is {x:.2f} dollars')

s="ddeded"
num=50
print(s+str(num))

items=["ab",'bv',"cd"]
print(items)
print(items.insert(1,'ff'))


point = (10, 20)
print(point[0])

# dictonary
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
print(student["name"])
student["gpa"]=3.8
print(student)


product = "Laptop"
price = 1200

print("The {} costs ${}.".format(product, price))

print("The {0} costs ${1}.".format(product, price))

num1=5+3*2
print(f"5+3*2={num1}")