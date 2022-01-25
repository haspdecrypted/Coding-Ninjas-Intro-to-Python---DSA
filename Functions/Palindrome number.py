def checkPalindrome(n):
    Revese = 0
    while n > 0:
        Remainder = n % 10
        n = int(n / 10)
        Revese = Revese * 10 + Remainder
    return Revese


num = int(input())
Rev=checkPalindrome(num)
if (num==Rev):
    print('true')
else:
    print('false')