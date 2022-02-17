from sys import stdin

def selection_sort(arr,n):
    for i in range(len(arr)):
        n = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[n]:
                n = j
        arr[i], arr[n] = arr[n], arr[i]
    return arr




#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    selectionSort(arr, n)
    printList(arr, n)

    t-= 1