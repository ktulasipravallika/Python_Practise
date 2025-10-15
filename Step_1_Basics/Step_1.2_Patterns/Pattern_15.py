'''
ABCDE
ABCD
ABC
AB
A
'''
n=int(input("Enter the count :"))
for i in range(1,n+1):
    for j in range(ord('A'),ord('A')+n-i+1):
        print(chr(j),end="")
    print()


from string import ascii_uppercase

for i in range(1, n + 1):
    print(ascii_uppercase[:n-i+1])
