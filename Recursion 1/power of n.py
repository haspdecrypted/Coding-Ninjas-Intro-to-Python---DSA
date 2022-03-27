def powerof(a, b):
    results=1
    for n in range(b):
        results=results*a
    return results
a,b=input().split()
a=int(a)
b=int(b)
print(powerof(a, b))