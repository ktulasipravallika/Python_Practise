age = int(input("Enter your age :"))

if age<0:
   print("not Valid")
elif age < 18 :
   print("Minor")
elif (age > 18 and age < 45) :
   print("Adult")
else :
   print("Senior")