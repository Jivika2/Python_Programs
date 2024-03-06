string='geeks quiz practice code'
s=string.split()[::-1]
#split() used to separate word in string
l=[]
for i in s:
    l.append(i)
print(l)
print(' '.join(l))

#function of reverse words in string
def rev_sentence(s):
    words=s.split(' ')
    rev_sentence=' '.join(reversed(words))
    return rev_sentence
if __name__=="__main__":
    input='geeks quiz practice code'
    print(rev_sentence(input))
#using backward iteration
import re
def rev_sentence(s):
    words=re.findall('\w+',s)
    reve_sentence=' '.join(words[i] for i in range(len(words)-1,-1,-1))
    return reve_sentence
if __name__=="__main__":
    input='geeks quize code'
    print(rev_sentence(input))
#using stack
string='geeks quiz practice code'
stack=[]
for word in string.split():
    stack.append(word)
reverse_words=[]
while stack:
    reverse_words.append(stack.pop())
print(reverse_words)
reverse_string=' '.join(reverse_words)
print(reverse_string)

#Revese words using split() python
def reverse_words(string):
    words=string.split()
    reversed_string=' '
    for i in range(len(words)-1,-1,-1):
        reversed_string+=words[i]+' '
    return reversed_string.strip()
string='geeks quiz practice code'
reversed_string=reverse_words(string)
print(reversed_string)

#Using Two point approach
def reverse_words(s,start,end):
    while start<end:
        s[start], s[end]=s[end],s[start]
        start+=1
        end-=1
def reverse_string(s):
    s=list(s)
    start, end=0, len(s)-1
    reverse_words(s,start,end)
    start=end=0
    while end<len(s):
        if s[end]==' ':
            reverse_words(s,start,end-1)
            start=end+1
        end+=1

    reverse_words(s,start,end-1)
    return ''.join(s)
s='geeks quize code'
print(reverse_string(s))

