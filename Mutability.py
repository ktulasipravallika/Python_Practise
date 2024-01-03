# Mutability is ability to change/edit the data in a specific memory location

# Tuple - immutable
a = (1, 2, 3, 4, 5)
print(id(a))

a = a + (6, 7)
print(a)

# New memory Location will be assigned, when there is a change to immutable data types
print(id(a))

# Similarly String - immutable

b = "Hello"
print(id(b))

b = b + "World"
print(b)
print(id(b))

# Mutable data types like Sets, Lists, Dictionary

L =[1, 2, 3, 4, 5, 6]
print(id(L))

L.append(7)
print(L)
print(id(L))

# The address will not be changed even if the values are changed/edited in a mutable data types

# Mutability should be handled carefully

L1 =[1, 2, 3]
print("The id of L1", id(L1))

L2 = L1
print("The id of L2", id(L1))

L2.append(5)
print(L2)
print(L1) # Changes L1 as well which is not expected as addresses are same

# To avoid this CLONING is used while copying

L3 = L1[:]

L3.append(6)

print(L3)
print(L1)
print(id(L1))
print(id(L3))


# Consider a tuple which is immutable have a list inside it which is mutable, the list inside it can be modified.

T1 = (1, 2, 3, 4, [5, 6])
T1[-1][-1]=900

print(T1)