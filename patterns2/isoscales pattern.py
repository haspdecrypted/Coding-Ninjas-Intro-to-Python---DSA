'''
   1
  121
 12321
1234321

'''

n=int(input())
i=1
while i<=n:
   #spaces
    space=1
    while space<=n-i:
        print(' ',end='')
        space+=1
    j=1
    p=1
    #increasing sequence
    while j<=i:
        print(p,end='')
        j+=1
        p+=1
    #decreasing sequence
    q=i-1
    while q>=1:
        print(q,end='')
        q-=1
    print()
    i+=1
