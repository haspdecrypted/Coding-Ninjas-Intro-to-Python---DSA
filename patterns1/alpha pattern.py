'''
A
BB
CCC
'''

n=int(input())
i=1
while i<=n:
    j=1
    start_char=chr(ord('A')+i-1)
    while j<=i:
        print(chr(ord(start_char)),end='')
        j+=1
    print()
    i+=1