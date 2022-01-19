'''
   1
  212
 32123
4321234

'''



n = int(input())
num = 1
gap = n - 1
for j in range(1, n + 1):
    num = j
    for i in range(1, gap + 1):
        print(" ", end="")
    gap = gap - 1

    for i in range(1, j + 1):
        print(num, end="")
        num-=1
    num=2
    for i in range(1, j):
        print(num, end="")
        num+=1

    print()