# import area

# print(area.area_fun(3))

# Create or overwrite a file

with open("output.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")
    file.write("Python file handling is easy!")

print("\n'output.txt' created/overwritten with new content.")