'''
   *
  ***
 *****
  ***
   *

'''

n=int(input())
firstHalf=(n+1)//2
secHalf=(n)//2

#First Half
currRow=1
while currRow<=firstHalf:
    spaces=1
    while spaces<=(firstHalf-currRow):
        print(' ',end="")
        spaces+=1
    currcol=1
    while currcol<=(2*currRow)-1:
        print("*",end="")
        currcol+=1
    print()
    currRow+=1

#Secound Half
currRow=secHalf
while currRow>=1:
    spaces=1
    while spaces<=(secHalf-currRow+1):
        print(" ",end="")
        spaces+=1
    currcol=1
    while currcol<=(2*currRow)-1:
        print("*",end="")
        currcol+=1
    print()
    currRow-=1
