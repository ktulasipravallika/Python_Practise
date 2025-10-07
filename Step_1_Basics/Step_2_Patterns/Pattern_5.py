'''
*****
****
***
**
*
'''
n=int(input("Enter count:"))
for i in range(1,n+1):
    for j in range(0,n+1-i):
        print("*", end="")
    print(" ")
