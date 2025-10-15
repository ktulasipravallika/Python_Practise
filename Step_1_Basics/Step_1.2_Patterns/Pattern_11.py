'''
1
01
101
0101
10101
'''

n=int(input("Enter count :"))
for i in range(1,n+1):
    if i%2==0:
        bit=0
    else:
        bit=1
    for j in range(1,i+1):
        print(bit, end="")
        bit =1-bit
        '''
        if bit==1:
            bit=0
        else:
            bit=1
        '''
    print()