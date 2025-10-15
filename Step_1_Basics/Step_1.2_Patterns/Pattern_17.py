'''
   A
  ABC
 ABCBA
ABCDCBA
'''

n=int(input("Enter the count:"))
for i in range(1,n+1):
    breakpoint=((2*i)+1)//2
    char='A'
    for j in range(n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        if j<=breakpoint:
            print(char,end="")
            char=char+1

        
    print()

    