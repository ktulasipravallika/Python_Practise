'''
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *
'''



n = int(input("Enter the number of rows of stars :"))
for i in range(1,2*n):
    if i<=n:
        for j in range(i):
            print("*", end="")
        print()
    else:
        for j in range(2*n-i):
            print("*", end="")
        print()
