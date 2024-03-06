def palindrome(s):
    mid=(len(s)-1)//2
    start=0
    last=len(s)-1
    flag=0
    while(start<=mid):
        if(s[start]==s[last]):
           start+=1
           last-=1
        
        else:
            flag=1
            break
    if flag==0:
        print('The entred string is palindrome')
    else:
        print('The entered string is not palindrome')
def symmetry(s):
    n=len(s)
    flag=0
    if n%2:
        mid=n//2+1
    else:
        mid=n//2
    start1=0
    start2=mid
    while(start1<mid and start2<n):
        if (s[start1]==s[start2]):
            start1+=1
            start2+=1
        else:
            flag=1
            break
    if flag==0:
        print('The entered string is symmetricsl')
    else:
        print('The entered string is not symmetrical')
s='amaama'
palindrome(s)
symmetry(s)

#using slicing method
s='amaama'
half=int(len(s)/2)
first_s=s[:half]
second_s=s[half:]
if first_s==second_s:
    print(s,'string is symmetrical')
else:
    print(s,'string is symmetrical')
if first_s==second_s[::-1]:
    print(s,'string is palindrome')
else:
    print(s,'string is not palindrome')

#using re module
import re
s='ammama'
w=s[::-1]
if(s==w):
    print('the string is symmetrical')
else:
    print('the string is not symmtrical')
#if re.match("^(\w+)\z",s)and s==s[::-1]:
 
if re.match("^(\w+)\Z", s) and s == s[::-1]:
    print('the entered string is palindrome')
else:
     print('the string is not palindrome')
#
# code
string ="malayalam"
print("the string is palindrome" if string==reversed(string) else "the string is not palindrome")

    
    
