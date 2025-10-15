## Check if the number is prime or not

import math


number = int(input("Enter any number :"))

if number==1: print("Not a Prime Number")
else:
    
    for i in range(2,int(math.sqrt(number)+1)):
        if number%i==0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")


