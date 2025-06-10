
num1 = int(input("Enter number1"))
num2 = int(input("Enter number2"))

if num1 == num2:
	print("Numbers are Equal")
else:
	if num1>num2:
		print("%3d is greater than %3d" %(num1, num2))
	else:
		print("%3d is greater than %3d" %(num2, num1))