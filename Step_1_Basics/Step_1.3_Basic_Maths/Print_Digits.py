# Print all the digits in a number

number= abs(int(input("Enter a number : ")))
print("The digits are :")
while number>0:
    print(number%10)
    number=number//10

