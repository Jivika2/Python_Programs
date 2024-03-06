def isPalindrome(s):
    return s==s[::-1]
s='malayalam'
ans=isPalindrome(s)
if ans:
    print('yes')
else:
    print('false')

#Not using iterative method

def isPalindrome(s):
    for i in range(0,int(len(s)/2)):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True

ans=isPalindrome(s)
if ans:
    print('yes')
else:
    print('false')

#Not using inbuilt function to reverse a string
#''.join(reversed(string)) predefined function
def isPalindrome(s):
    rev=''.join(reversed(s))
    print(rev)
    if(s==rev):
        return True
    else:
        return False
s='malayalam'
ans=isPalindrome(s)
print(ans)
if ans:
    print('yes')
else:
    print('no')

#using one extra variable
x='malayalam'
w=''
for i in x:
    w=i+w
print(w)
if(x==w):
    print('yes')
else:
    print('No')
#using flag
s='malayalam'
j=-1
flag=0
for i in s:
    if i!=s[j]:
        flag=1
        break
    j=j-1
if flag==1:
    print('false')
else:
    print('true')

#using recursion
def isPalindrome(s):
    s=s.lower()
    l=len(s)
    if l<2:
        return True
    elif s[0]==s[l-1]:
        return isPalindrome(s[1:l-1])
    else:
        return False
s='malayalam'
ans=isPalindrome(s)
if ans:
    print('yes')
else:
    print('false')

