'''
A
BB
CCC
DDDD
EEEEE
'''


n=int(input("Enter the count:"))

for i in range(1,n+1):
    alpha=ord('A')+i-1
    for j in range(1,i+1):
        print(chr(alpha),end="")
    #alpha=alpha+1
    print()