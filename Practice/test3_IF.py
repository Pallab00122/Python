sugar_level=input(print("Enter your sugar level:"))
sugar_level=int(sugar_level)
if sugar_level< 80:
    print("Low")
elif sugar_level>100:
    print("High")
else:
    print("Your sugar is normal, relax and enjoy your life!")