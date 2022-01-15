#Write Your Code Here
n=int(input())
rev_num=0
while n>0:
    remainder=n%10
    rev_num=(rev_num*10)+remainder
    n//=10
    
print(rev_num)