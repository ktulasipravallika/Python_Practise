# List can be heterogeneous
# Consists of multiple types of data
# Memory locations are not continuous
# Lists are more programer freindly

List1 = ["Hello", 2, 3.5, True, 5+9j]
print(List1)

#2D List

List2 = [1, 2, [3,4,5]]
print(List2)

#3D List

List3 = [1, 2, [3,4,[5,6,7],8,9],10]
print(List3)

List4 = list("Tulasi")
print(List4)

List5= list()
print(List5)

#Accessing the list item

List1[0] ="World"
print(List1)

a = List2[2]
print(a[1])

#Accessing the inner list elements

print(List3[2][2][2])

# Edit

List2[0:4] = [1,2,3,5,6]
print(List2)

#Append

List2.append("Hi..!") # Can add 1 item in the last 
List2.append([80,90]) # adds as one single inner list item
print(List2)

#Extend

List2.extend([10,20,30]) # Can add multiple items in the last
print(List2)

# Insert

List2.insert(1,"World")
print(List2)

# Delete(del, pop, remove, clear)

del List2
#print(List2) # List2 is deleted

del List1[1]
print(List1)

List1.remove("World")
print(List1)

List1.pop() # deletes the last item
print(List1)

List1.clear()
print(List1) # Just clears and empties the list items

L = [1, 2, 3, 4]
L1 = [5, 6, 7, 8]
L2 = L + L1*3
print(L2)

for i in List3 :
    print(i)

# directly 4 is not present in List3 , $ is in the inner List
print(4 in List3)

# Functions in List

print(len(L2))
print(min(L2))
print(max(L2))
print(sorted(L2)) # creates a new list

print(len(L2))
print(L2.index(5))