def printTable(start,end,step):
    while start <= end:
        Fahrenheit_to_Celsius = (((start - 32) * 5) / 9)
        print(start, int(Fahrenheit_to_Celsius))
        start = start + step
  
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)
