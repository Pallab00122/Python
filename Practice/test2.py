india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# city=input(print("Enter the city name: "))

# if city  in india:
#     print(f"{city} is in india")

# elif city in pakistan:
#     print(f"{city}in pakisthan")
# else:
#     print("Not Listed") 

city1 = input("Enter city 1: ")
city2 = input("Enter city 2: ")

if city1 in india and city2 in india:
    print("Both cities are in india")
else:
    print("They don't belong to same country")