'''
1234
123
12
1
'''

n=int(input())
i=0
while(i<n):
    j=1
    while(j<n-i+1):
        print(j,end='')
        j+=1
    i+=1
    print()