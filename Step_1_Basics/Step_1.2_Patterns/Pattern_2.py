'''
*
**
***
****
*****
'''
n=int(input("Enter count:"))
for i in range(n):
    for j in range(0,i+1):
        print("*", end="")
    print("")