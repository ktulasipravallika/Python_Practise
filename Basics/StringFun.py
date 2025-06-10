# Common Functions

c = "vijayawada"
print(len(c))
print(max(c))
print(min(c))
print(sorted(c, reverse=True)) # reverse = "True indiacates descending order"
print(sorted(c)) # default prints in ascending order.

# Captalise/ Title /Upper / Lower / Swapcase

print(c.capitalize()) # first letter will be capitalised
print("it is raining today ".capitalize())
print("it is raining today ".title())
print("it is raining today ".upper())
print("IT IS raining today ".lower())
print("IT IS raining today ".swapcase())

# Count

print("it is raining today ".count('t'))

# Find / Index

print("it is raining today ".find('t')) # indexof first occurance is displayed
print("it is raining today ".find('rain'))
print("it is raining today ".find('fadffad')) # if not found give -1

print("it is raining today ".index('t')) # indexof first occurance is displayed
print("it is raining today ".index('rain'))
#print("it is raining today ".index('adsfadsf')) # if not found throws error

# endswith /startswith

print("it is raining".endswith("sdsas"))
print("it is raining".endswith("raining"))
print("it is raining".startswith("is"))
print("it is raining".startswith("it"))

# format

a = "Hello my name is {} and I am {}".format("Tulasi", 28)
print(a)

b = "Hello my name is {name} and I am {age}".format(name = "Tulasi",age= 28 , weight = "70")
print(b)

# isalnum/ isalpha / isdecimal/isdigit / isidentfier

print("FLAT20&".isalnum())
print("FLAT20&".isalpha())
print("&".isdigit())
print("20".isdecimal())

# Split

print("who is the prime minister of india?".split())
print("who is the prime minister of india?".split("prime"))
print("who is the prime minister of india?".split("zxsaafads"))

# Join

print("-".join(['who', 'is', 'the', 'prime', 'minister', 'of', 'india?']))
print(" ".join(['who', 'is', 'the', 'prime', 'minister', 'of', 'india?']))

#Replace

a = "Hi my name is Tulasi".replace("Tulasi","Pravallika")
print(a)

# Strip

name = "     dsfa    "
print(name.strip())