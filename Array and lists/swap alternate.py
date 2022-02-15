def swapAlternate (li):
    length =len(li)
    i = 0
    for k in range(length//2):
        li[i],li[i+1]=li[i+1],li[i]
        i+=2
    print(*li,end=" ")
    print()

loop_cycle=int(input())
for i in range(0, loop_cycle):
    faltu = input()
    lip = [int(x) for x in input().split()]
    swapAlternate(lip)
    
