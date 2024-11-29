#to check a number is prime or not
num=int(input("Enter a number to check:\n"))
flag=False
if num==1:
    print(num,"is not prime.")
elif num>1:
    for n in range(2,num):
        if (n%num==0):
            flag=True
        break
    if flag:print(num,"is not prime.")
    else:print(num,"is prime")
