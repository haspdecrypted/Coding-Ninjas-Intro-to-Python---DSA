'''
ABCD
BCDE
CDEF
DEFG
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
    start_char=chr(ord('A')+i-1)
    while j<=n:
        print(chr(ord(start_char)+j-1),end='')
        j+=1
    print()
    i+=1
   