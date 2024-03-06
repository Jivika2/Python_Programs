'''list=[12,13,45,66]
sum=0
for i in list:
    sum=sum+i
print('sum of given list:',sum)

#using while loop
list=[12,23,45,23.12]
sum=0
i=0
while(i<len(list)):
    sum=sum+list[i]
    i+=1
print('Sum of given list is:',sum)

#using recursive way
list=[12,14,27,98]
def sumOfList(list,size):
    if(size==0):
        return 0
    else:
        return list[size-1]+sumOfList(list,size-1)
sum=sumOfList(list,len(list))
print(sum)

#using sum()

# Python program to find sum of elements in list
 
# creating a list
list1 = [11, 5, 17, 18, 23]
 
# using sum() function
total = sum(list1)
print(total)'''

#using add()operator module
from operator import*
list=[12,14,4,10]
result=0
for i in list:
    result=add(result,i)
print(result)

#using enumerate function
list=[2,3,4,6,7,8,9]
s=0
for i,a in enumerate(list):
    s+=a
print('sum is:',s)

#using list comprehension
list=[12,13,15]
s=[i for i in list]
print(sum(s))

'''#using lambda function
list=[12,14,56,5]
sum=0
print(sum(list(filter(lambda x:(x),list))))

#using add operator
import operator
s=0
list=[23,1,45,6,12]
for i in list:
    s=s+operator.add(0,i)
print(s)'''

#using add()+while loop
import operator
list=[12,13,24,5,6]
sum=0
i=0
while(i<len(list)):
    sum=sum+operator.add(0,list[i])
    i+=1
print('Sum of the list :',sum)


