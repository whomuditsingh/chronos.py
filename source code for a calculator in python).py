#source code for a calculator in python
num1,num2=map(float,(input("enter two numbers separated by spaces: ")).split())
op=input("enter operator:")
print(num1,"\n",num2,"\n",op,"\n")
if op=="+":
    print(f"result is:{num1+num2}")
elif op=="-":
    print(f"result is:{num1-num2}")
elif op=="*":
    print(f"result is:{num1*num2}")
elif op=="/":
    print(f"result is:{num1/num2}")
else:
    print("invalid operator,TRY AGAIN!!")

