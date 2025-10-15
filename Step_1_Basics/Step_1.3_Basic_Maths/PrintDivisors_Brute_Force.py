### Brute Force - Time Complexity = O(n)

number = int(input("Enter any number: "))

print(f"The divisors of the given number {number} are: ")
for i in range(1,number+1):
    if (number%i)==0:
        print(i)

