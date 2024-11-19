#GENERATION OF RANDOM NUMBERS BY USER DEFINED
#Take input from users
a,b=map(float,input("enter two numbers separated by spaces: ").split()) 
print(a,b)
import random
random_num=random.randrange(a,b)
print(random_num)