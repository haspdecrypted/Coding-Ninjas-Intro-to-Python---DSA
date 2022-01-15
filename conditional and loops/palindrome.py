def checkPalindrome(num):
    rev_num=0
    while num>0:
        remainder=num%10
        rev_num=(rev_num*10)+remainder
        num=int(num/10)
    return rev_num
		
num = int(input())
if(num==checkPalindrome(num)):
	print('true')
else:
	print('false')
