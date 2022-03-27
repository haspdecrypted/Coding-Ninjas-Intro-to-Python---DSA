def checkNumber(arr, x):
    i=0
    while i<=n-1:
        if arr[i]==x:
            return True
        
        else:
            i=i+1
            
    # Please add your code here

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')