'''
ABCD
ABCD
ABCD
ABCD
'''
'''
k=int(input())
x=ord('A')
ascii_target=x+k-1
target_char=chr(ascii_target)
#print(target_char)
'''
n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        print(chr(ord('A')+j-1),end='')
        j+=1
    print()
    i+=1
   