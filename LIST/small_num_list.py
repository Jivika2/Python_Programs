#using sorting
list=[23,56,3,67,89]
list.sort()
print('smallest number of the list:',list[0])
#in descending order
list.sort(reverse=True)
print('smallest number of the list:',list[-1])

#using min() method
list=[12,345,66,65,0]
print('smallest number of list :',min(list))

#using user defined list
'''list=[]
num=int(input('Enter number of elements in list:'))
for i in range(1,num+1):
    ele=int(input('Enter elements:'))
    list.append(ele)
print('smallest element is:',min(list))

#comparing every element
#l=[12,34,57,67,46,8]
l=[int(l) for l in input('list:').split(',')]
print('The list is',l)
min1=l[0]
for i in range(len(l)):
    if l[i]<min1:
        min1=l[i]
print('smallest element in the list is:',min1)'''

#using lambda function
lst=[12,3,4,5,66,12]
print(min(lst, key=lambda value: int(value)))

#using enumerate function
lst=[12,34,56,7,8]
a,i=min((a,i) for (i,a) in enumerate(lst))
print(a)

#using reduce function
from functools import reduce
lst=[12,45,7,8,9]
print(reduce(min,lst))

#using heap
import heapq
def find_smallest(numbers):
    #Build a min heap using the elements in the list
    heap=[(x,x) for x in numbers]
    heapq.heapify(heap)
    _,smallest=heapq.heappop(heap)
    return smallest
numbers=[10,20,4,5,34]
print(find_smallest(numbers))



def Findsmall(itr,ele,list1): #recursive function to find smallest number
  if itr == len(list1):        #base condition
    print("The smallest number in the list is " ,ele)
    return
  if list1[itr]<ele: #check the current element less than minimum or not
    ele  =  list1[itr]
  Findsmall(itr+1,ele,list1) #recursive function call
  return
#driver code
lis=[5,7,2,8,9]
ele = lis[0]
Findsmall(0,ele,lis)
