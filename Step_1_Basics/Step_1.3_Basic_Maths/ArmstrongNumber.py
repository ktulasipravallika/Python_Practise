# Armstrong Number

number = int(input("Enter a number :"))
temp=number
sum=0
count=0
t=number
while t>0:
    count+=1
    t=t//10

t=number
while t>0:
    digit=t%10
    sum=sum+(pow(digit,count))
    t=t//10

if sum==temp: 
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
