num=int(input())
s_o_e=0
s_o_o=0
while num>0:
    remainder=num%10
    if(remainder%2==0):
        s_o_e+=remainder
    else:
        s_o_o+=remainder
    num//=10
print(s_o_e,s_o_o)
        