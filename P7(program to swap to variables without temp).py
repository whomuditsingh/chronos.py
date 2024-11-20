#program to swap to variables without temp variables
a,b=map(float,(input("enter two number separated by spaces:\n")).split())
print(a,b)
a,b=b,a
print("After swapping:")
print("a=",a)
print("b=",b)
