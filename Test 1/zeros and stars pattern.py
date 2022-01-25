n=int(input())
start=1
end=2*n+1
mid=n+1
row=1
while(row<=n):
    column=1
    while column<=(2*n+1):
        if column==start or column==end or column==mid:
            print("*",end='')
        else:
            print("0",end='')
        column=column+1
    start+=1
    end-=1
    row+=1
    print()