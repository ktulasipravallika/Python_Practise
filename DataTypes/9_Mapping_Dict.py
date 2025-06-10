students ={}
studentCount=int(input("Enter number of Students:"))

for i in range(studentCount) :
    name=input(f"Enter the name of the Student {i+1}")
    marks=float(input(f"Enter the marks of the Student {i+1}"))
    students[name]=marks


print("Student with marks above 70 :")

for name,marks in students.items():
    if marks>=70 :
        print(name)
    