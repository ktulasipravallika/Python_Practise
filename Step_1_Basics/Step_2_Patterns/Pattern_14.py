'''
A
AB
ABC
ABCD
ABCDE
'''
n=int(input("Enter the count :"))
for i in range(1,n+1):
    for j in range(ord('A'),ord('A')+i):
        print(chr(j),end="")
    print()


from string import ascii_uppercase

for i in range(1, n + 1):
    print(ascii_uppercase[0])
