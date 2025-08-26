# book={}
# book['Tom']={
#     'name':'Tom',
#     'phone':9856665455
# }
# book['Bob']={
#     'name':'Bom',
#     'phone':9855645654
# }

# import json
# s=json.dumps(book)
# # print(s)
# with open ("F://data//book.txt","w") as f:
#     f.write(s)

f=open("F://data//book.txt","r")
f_out=open("F://data//book_bb.txt","w")
for line in f:
    tokens=line.split(" ")
    f_out.write("Wordcount " + str(len(tokens))+line)
# f.write("Python")
# print(f.read())
f.close()
f_out.close()