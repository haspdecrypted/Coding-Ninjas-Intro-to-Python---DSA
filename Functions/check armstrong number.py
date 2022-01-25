n=int(input())
no_of_digits=0
org_n=n
orginal_no=n
Armstrong=0
while n>0:
    no_of_digits+=1
    n=n//10
while org_n>0:
    Last_Digit = org_n % 10
    Armstrong  = Armstrong  + ((Last_Digit)**(no_of_digits))
    org_n = (org_n //10)
if orginal_no==Armstrong:
    print("true")
else:
    print("false")