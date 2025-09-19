age=int(input("Enter your age :"))

if age<18:
    print("Not eligible for Job")
elif age<57:
    print("Eligible for Job", end='')
    if age>=55:
        print(", but retirement soon")
else:
    print("retirement time")

