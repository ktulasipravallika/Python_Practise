# Sets do not allow duplicate data
# Sets have no indexing/slicing
# Sets do not allow mutable data types like lists, sets
# Sets is a mutable data type- 2D and 3D sets are not possible

S1 = {}
print(type(S1)) # dictionary

S2 = set()
print(type(S2))

# Homogeneous Data
S3 = {1, 2, 3, 4, 5, 6}

# Heterogeneous Data
S4 = {"Hello", 4.5, 332, 'c', 32}

# Duplicates are not allowed
S5 = {1, 1, 2, 2, 3, 4, 5, 3, 5}
print(S5)

# Mutable data types are not allowed

# S6 = {[1, 2, 3],"Hello"}
# S6 = {{1, 2, 3},"Hello"}

S6 = {(1, 2, 3),"Hello"}
print(S6)

# Cannot access items seperately from sets 

S7 = {1, 2, 3, 4, 6, 7, 8}
# print(S7[3])

# Slicing is also not possible
# print(S7[-1, -5])

# Add items

S7.add(77)

# addressof set 

print(id(S7))
print(S7)

# Deleting sets

# del(S3[2]) - not allowed as indexing is not allowed
# print(S3)

del S2
# print(S3) - cannot print after deleting

# removing element in set
S3.remove(3)
print(S3)

# pop() - removes the last element in the set - Due to hashing, the first elelment in the set w

S3.pop()
print(S3)

S8 = {1, 2, 3, 4, 5, 6}
S9 = {6, 7, 8, 9, 10}

# S10 = S8 + S9 - Not supported
# S11 =S8 * 6 - Not supported


# Loops
for i in S8 :
    print(i)

# Membership Operators

print(10 in S8)

print(len(S8))
print(min(S8))
print(max(S8))
print(sum(S8))
print(sorted(S8))
print(sorted(S8, reverse = True))
print(S8.union(S9))
print(S8.intersection(S9))
print(S8.difference(S9))
print(S9.difference(S8))
print(S8.symmetric_difference(S9))
print(S8.isdisjoint(S9))
print(S8.issubset(S9))
print(S8.issuperset(S9))
S9.clear()
print(S9)
