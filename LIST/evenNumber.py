'''for i in range(2,18,2):
    if i%2==0:
        print(i, end=' ')'''
def odd(num1,num2):
    if num1>num2:
        return
    if (num1&1)!=0:
      print(num1,end=" ")
      return odd(num1+2,num2)
    else:
      return odd(num1+1,num2)
n1=4;n2=15
odd(n1,n2)

result=[i for i in range(2,17,2) if i%2!=0]
print('\n odd numbers:',result)
li=[]
for i in range(n1,n2+1):
    li.append(i)
    
print(li)

result=list(filter(lambda x: (x%2!=0),li))
print(result)

for num in range(4,20):
       if  (num & 1):
 
        print(num, end = " ")
