# Creating two complex numbers
num1 = 2 + 3j
num2 = 4 + 5j

sum_result = num1 + num2

mul_result = num1 * num2


print("First Complex Number:", num1)
print("Second Complex Number:", num2)

print("\nSum:", sum_result)
print("Multiplication:", mul_result)

print("\nSum - Real Part:", sum_result.real)
print("Sum - Imaginary Part:", sum_result.imag)

print("\nMultiplication - Real Part:", mul_result.real)
print("Multiplication - Imaginary Part:", mul_result.imag)
