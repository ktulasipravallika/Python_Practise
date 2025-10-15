# Palindrome Or Not

number = int(input("Enter a number: "))
temp=number

reverse_number = 0

while temp>0:
    digit=temp%10
    reverse_number=(reverse_number*10)+digit
    temp=temp//10

if reverse_number==number:
    print("The number entered is a palindrome")
else:
    print("Not a Palindrome")
