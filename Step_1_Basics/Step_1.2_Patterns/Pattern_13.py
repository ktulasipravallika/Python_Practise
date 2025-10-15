'''
1
23
456
78910
1112131415
'''
n=int(input("Enter the count :"))
number=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(number,end="")
        number=number+1
    print()