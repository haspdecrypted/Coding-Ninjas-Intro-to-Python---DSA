from sys import stdin
def arePermutation(str1, str2):
    n1 = len(str1) 
    n2 = len(str2)
    if (n1 != n2):
        return False
    
    freq = [0]*256
    
    for i in range(n1):
        ch = ord(str1[i])
        freq[ch] += 1
        
    for i in range(n2):
        ch = ord(str2[i])
        freq[ch] -= 1
    
    for i in range(256):
        if freq[i] != 0:
            return False
    return True
        
    
    
  
str1 = stdin.readline().strip()
str2 = stdin.readline().strip()
ans = arePermutation(str1, str2)
if ans:
    print("true") 
else: 
    print("false") 