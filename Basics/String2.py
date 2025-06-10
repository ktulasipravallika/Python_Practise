c = "Hello"

# Strings are immutable data types i.e changes are not allowed.
# c[0] ='X'
# print(c)

# Strings can be reassigned to new word.
c = "World"
print(c)

# Cannot add new characters at end or anywhere.
# c[5]= 'W'
# print(c)

# Cannot delete any character in a string.
# del c[0]
# print(c)

# Arithmetic Operations
a = "Hello " + "World"
print(a)

print("Welcome..." * 10)

# Relational Operations
print("Hello" == "World")
print("Hello" != "World")
print("Hello" > "World") # Lexiographically checks for the >, <, >=, <= --> Checks for the dictioanlry order
print("Hello" < "World")
print("Hello" >= "World")
print("Hello" <= "World")

#Logical Operations

# Empty String is considered as "False" and
# Any Non Empty String is considered as "True"

print("hello" and "world")
print("hello" or "world")
print(not "hello")
print("" and "hello")
print("" or "hello")
print(not "")

# Loops

c = "Hello World"
for i in c :
    print(i)

# Membership Operators

print('h' in c)
print('H' in c)
print('z' in c)
print('r' in c)
print('ff' in c)
print('sdf' in c)