'''
E
DE
CDE
BCDE
ABCDE
'''

n=int(input())
i=1
while i<=n:
    j=1
    char=ord('A')+n-i
    while j<=i:
        print(chr(char+j-1),end="")
        j+=1
    print()
    i+=1  
    