# count number of digits in the number given.
number=abs(int(input("Enter the number : ")))
count=1 if number==0 else 0
while number>0:
    number=number//10
    count+=1
print(count)

