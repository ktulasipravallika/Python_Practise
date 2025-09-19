# Multuple inputs - Strings

name1, name2 = input("Enter your first name and last name:").split()

print("Hi", name1)
print("Your username is:", name2)


# Multuple inputs - integers

x, y = map(int, input("Enter 2 numbers:").split())

print("x+y=", x+y)

