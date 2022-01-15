n=int(input())
flag=False
d=2
while d<n:
    if n % d == 0:
        flag = True
    d +=1
if flag:
    print("Not Prime")
else:
    print("Prime")