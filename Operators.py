#Arithmetic Operators

a = 104
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b) # converts the output to integer Ex : 5/2 = 2.5 but shows 2 as output.

# Reltional / Comparision operators

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

# Logical operators

x = True 
y = False

print(x and y)
print(x or y)
print(not x)

# Bitwise operators

print(a & b)
print(a | b)
print(x >> 2)
print(y << 3)


# Assignment Operator

a = 3;
a+= 10;
a-= 10;
a*=100;
a/= 2;
print(a)


# Identity Operator

a = "Tulasi"
b = "Tulasi"
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)


# Membership Operator

x = [1, 2, 3, 4, 5] # can be a Tuple (()), set {} or dictionary {"":"",}
print(6 in x)
print(6 not in x)
print(5 in x)