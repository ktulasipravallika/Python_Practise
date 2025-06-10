set1=set()
set2=set()

set1Count= int(input("Enter number of elements in set 1 :"))
set2Count= int(input("Enter number of elements in set 2 :"))

for i in range(set1Count):
    num=int(input(f"Enter the element {i+1}: in set1 :"))

    set1.add(num)

print("Elements in set1: ",set1)

for i in range(set2Count):
    num=int(input(f"Enter the element {i+1}: in set2 :"))

    set2.add(num)


print("Elements in set2: ",set2)

print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Difference:", set1.difference(set2))


