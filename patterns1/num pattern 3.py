'''
1
11
121
1221
'''

n=int(input())
i=1
print(1)
while i<=n-1:
    print("1",end="")
    num_2=2
    while num_2<=i: #no of Colums
        print("2",end="")
        num_2+=1
    print("1")
    i=i+1