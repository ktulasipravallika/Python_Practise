number= int(input("Enter a number to check if it is even or not"))

if number==0:
    print("Number is neither Even Nor Odd")

else :
    if number%2==0:
        print("%3d is even number : True" %number)
    else:
        print("%3d is even number :False " %number)
