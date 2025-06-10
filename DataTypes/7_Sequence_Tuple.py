print("Enter the tuple elements")

elements=[]
for i in range(5) :
    num= float(input(f"Enter element {i+1} :"))
    elements.append(num)

tuple1=tuple(elements)

print(tuple1)


               