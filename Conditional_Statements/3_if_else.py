marks = float(input("Enter your marks: "))

if marks <100:
    if marks >= 90:
        print("Grade is : A")
    elif marks >=80:
        print("Grade is : B")
    elif marks >=70:
        print("Grade is : C")
    elif marks >=60:
        print("Grade is : D")
    elif marks<60:
        print("Grade is : F")
else:
    print("Enetr valid marks")
