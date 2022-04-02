# All the recursion assignment-code

-> Geometric Sum

def geometric(n):
    
    if n == 0:
        return 1
    return 1/pow(2,n)+ geometric(n-1)

n = int(input())
val = geometric(n)
print('%.5f' % val)

-> Check Palindrome (recursive)

def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False


a = str(input())
if(is_palindrome(a) == True):
    print("true")
else:
    print("false")

-> Sum of digits (recursive)

def sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum(n//10)


n = int(input())
print(sum(n))

-> Multiplication (Recursive)

def pro(m, n):
    if m == 0 or n == 0:
        return 0
    elif m < n:
        return n + pro(m-1, n)
    else:
        return m + pro(m, n-1)


m = int(input())
n = int(input())
print(pro(m, n))

-> Count Zeros

def count(n):
    if n == 0:
        return 1
    if n < 10:
        return 0
    elif n % 10 == 0:
        return count(n//10) + 1
    return count(n//10)
    
n = int(input())
print(count(n))

-> String to Integer

def strConv(s, li):
    # print(li)
    if len(s) == 0:
        return li
    else:
        li.append(ord(s[0]) - 48)
        return strConv(s[1:], li)


s = input()

li = []
li = strConv(s, li)
sum = 0
for i in range(len(li)):
    sum = sum * 10 + li[i]

print(sum, end="")

-> Pair Star

def func(s):
    if len(s) == 1:
        return s

    elif s[0] == s[1]:
        return s[0] + "*" + func(s[1:])

    else:
        return s[0] + func(s[1:])


s = input()
print(func(s))

-> Check AB

def abb(s, flag, bflag):
  if len(s) == 0:
    return flag

  elif s[0] == "a":
    flag = True
    bflag = False
    return abb(s[1:], flag, bflag)

  elif s[0] == 'b' and s[1] == 'b':
    if bflag == True:
      return False
    else:
      bflag = True
      return abb(s[2:], flag, bflag)
  
  else:
    return False



s = input()
flag = True
bflag = False
if s[0] == "a":
  x = abb(s, flag, bflag)
else:
  x = 0
if x:
  print("true")
else:
  print("false")

-> Staircase

def stair(n):

    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return stair(n-3) + stair(n-2) + stair(n-1)


n = int(input())
print(stair(n))