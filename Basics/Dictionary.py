# Dictionary has no indexing
# Dictionary is a mutable type
# Keys are immutable values, Values can be mutable
# Keys should be unique

# Mutable Data Types - Lists, Sets, Dictionary
# Immutable - String, Tuple, int, Float , Boolean, Complex

# Create a dictioanry

D = {}
print(D)

D = {"Name" : "Tulasi", "Age" : "27" }
print(D)

# Mutable keys are not allowed
# D1 = {[1, 2, 3] : "Tulasi"} - list as a key is not allowed as Lists are mutable

# Tuple Keys are allowed as Tuplease are immutable
D1 = {(1, 2, 3) : "Tulasi"}
print(D1)

# Same key values in a dictionary will not be allowed - will not throw error, but updates the last value to the key.

D2 = {"Name" : "Tulasi", "Name" : "Pravallika"}
print(D2)

# 2D dictionary
D3 = {"Name" : "Tulasi", "Age" : "27", "Marks" : {"M1" : "100", "C" : "90", "DS" : "80"}}
print(D3)

# Accessing values from dictionary

# print(D3[0])- Bot allowed,dictionary values can only be accessed by keys

print(D3["Name"])
print(D3["Age"])
print(D3["Marks"]["DS"])

# Edit

D3["Name"] = "Pravallika"
print(D3)

D3["Marks"]["C"] = "95"
print(D3)
print(D3.get("Age"))

# Add New key - value pair

D3["Gender"] ="Female"
D3["Marks"]["DB"] = "98"
print(D3)

# Delete

del(D)
# print(D) - cannot be accessed after deleting
del D3["Gender"]
del D3["Marks"]["DB"]
print(D3)


# D1 + D2 and D1 * 3 - Not allowed

# Loop
for i in D3:
    print(i, D3[i])

# Membership Operators

print("Pravallika" in D3)
print("Name" in D3)

# Functions

print(len(D3))
print(min(D3)) # - lexographical comparision
print(max(D3)) # - lexographical comparision
print(sorted(D3))
print(sorted(D3, reverse = True))
D3.keys
D3.values
