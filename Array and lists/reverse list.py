# reverse of a list

def rev_l(li):
    length=len(li)
    
    for i in range(length//2):
        #li[i],li[length-i-1]=li[length-i-1],li[i] #a,b=b,a 
        li[i],li[-i-1]=li[-i-1],li[i] 
        
li=[1,2,3,4,5,6,7]
rev_l(li)
print(li)