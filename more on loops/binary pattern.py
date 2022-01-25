'''
1111
000
11
0
'''
n=int(input())
for i in range(1,n+1):
    for j in range(n+2-2*i,0,-1):
        print(1,end="")
    print()
    for k in range (n+1-2*i,0,-1):
        print(0,end="")
    print()