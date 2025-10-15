# Print the digits in order

number = int(input("Enter a number :"))

temp=number
pow=1

while temp>=10:
    temp//=10
    pow=pow*10

while pow>=1:
    print(number//pow)
    number%=pow
    pow//=10