numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):

    value = input(f"Enter element {i + 1}: ")
    numbers.append(value) 

print("Dynamic Array:", numbers)



numbers.append('Pravallika')
numbers.remove('22')
numbers.insert(1,'Tulasi')
numbers.pop()

print("Modified List of elements: ", numbers)