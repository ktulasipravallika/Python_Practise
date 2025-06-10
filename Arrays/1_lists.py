numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):

    value = input(f"Enter element {i + 1}: ")
    numbers.append(value) 

print("Dynamic Array:", numbers)


print("Third Element in the list enetered is :", numbers[2])
print("Last Element in the list enetered is :", numbers[-1])
print("Element from 2 to last in the list enetered is :", numbers[1:])


numbers[2] = 'Tulasi'
print("Entered List of elements after modifying are: ", numbers)
