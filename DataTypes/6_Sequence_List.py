list1 = []

print("Enter the list of 5 numbers")

for i in range(5) :
    num=float(input(f"Enter the number {i+1} : "))
    list1.append(num)

addition=sum(list1)
average= addition/4
print("Addition : ", addition)
print("Average : ", average)