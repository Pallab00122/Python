result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for item in result:
    if item == "heads":
        count +=1
print("Heads count :",count)


for i in range(1,11):
    if i%2==0:
        continue
    print(i*i)


# expense_list = [2340, 2500, 2100, 3100, 2980]
# month_list = ["January", "February", "March", "April", "May"]
# e=input(print("Enter the expence: "))
# e=int(e)
# month=-1
# for i in range(len(expense_list)):
#     if e==expense_list[i]:
#         month = i
#         break
# if month != -1:
#     print(f"expense {e} found in {month_list[month]}")
# else:
#     print("expense not found ")


# for i in range(2,5):
#     print(f"you can run{i+1} miles")
#     tried=input("Are you tried ?")
#     if tried == 'yes':
#         break
# if i == 4: 
#     print("Hurray! You are a rock star! You just finished 5 km race!")
# else:
#     print(f"You didn't finish 5 km You still ran {i+1} miles")



for i in range(0,6):
    s=''
    for j in range(i):
        s=s+'*'
    print(s)
