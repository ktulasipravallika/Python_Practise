marks = int(input("Enter the marks"))

if marks<25:
    print("Grade is F")
elif marks<=44:
    print("Grade is E")
elif marks<=49:
    print("Grade is D")
elif marks<=59:
    print("Grade is C")
elif marks<=79:
    print("Grade is B")
elif marks<=100:
    print("Grade is A")
else:
    print("Enter the correct marks")