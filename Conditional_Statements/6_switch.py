month=input("Enter a Operation :")

number1 = int(input("Enter a number :"))
number2 = int(input("Enter a number :"))

match(month):

    case '+':
        print("Addition of number1 and number2 is :", number1+number2)
    case '-':
        print("Addition of number1 and number2 is :", number1-number2)
    case '*':
        print("Addition of number1 and number2 is :", number1*number2)
    case '%':
        print("Addition of number1 and number2 is :", number1%number2)
    case '/':
        print("Addition of number1 and number2 is :", number1/number2)

    case _:
        print("Enter a valid operation")