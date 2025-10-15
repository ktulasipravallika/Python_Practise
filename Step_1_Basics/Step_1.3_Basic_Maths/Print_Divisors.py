### Time Complexity = O(sqrt.n)
import math
number = int(input("Enter any number :"))
divisors=[]

print(f"The divisors of {number} are :")

for i in range(1,int(math.sqrt(number))):
    if number%i==0:
        divisors.append(i)
    if number//i!=i:
        divisors.append(number//i)
divisors.sort()
print(divisors)

