#swapping of values
a=float(input("enter a number:"))
b=float(input("enter a number:"))
print(f"original values:{a},{b}")
temp=a
a=b
b=temp
print("value of new variable a:{},variable of new variable b:{}".format(a,b))