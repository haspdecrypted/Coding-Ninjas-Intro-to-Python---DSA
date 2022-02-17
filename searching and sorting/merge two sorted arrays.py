def mergesorted(arr1, arr2):
    i = 0
    j = 0
    len1 = len(arr1)
    len2 = len(arr2)
    arr = []
    while ((i < len1) and (j < len2)):
        if (arr1[i] < arr2[j]):
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    while (i < len1):
        arr.append(arr1[i])
        i += 1
    while (j < len2):
        arr.append(arr2[j])
        j += 1
    return arr


loop = int(input())
for l in range(loop):
    arr1 = []
    arr2 = []
    ele1=int(input())
    if ele1!=0:
        arr1=[int(c) for c in input().split()]
    ele2=int(input())
    if ele2!=0:
        arr2=[int(v) for v in input().split()]
    arr=mergesorted(arr1,arr2)
    print(*arr)