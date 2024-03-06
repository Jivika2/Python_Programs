#clear a list by reinitializing the list
list=[19,1,3]
print('List before deleting is:' +str(list))
#deleting using reinitialization
list=[]
print('List after clearing using reinitialization:',list)

#using '*=0'
list=[193,34,32,45]
print('List before deleting is:' +str(list))
list*=0
print('List after using *=0 is:' +str(list))


#using del

list1=[1,3,5]
list2=[5,7,2]
print('List1 before deleting is:' +str(list1))
del list1[:]
print('List1 after using del is:' +str(list1))

print('List2 before deleting is:' +str(list2))
del list2[:]
print('List2 after deleting is:' +str(list2))


#using pop() method
list=[2,4,5]
print('List before deleting is:' +str(list))
while(len(list)!=0):
    list.pop()
print('List after deleting is:' +str(list))


#using slicing
list=[1,2,3,4,5,6,7]
print('List before deleting is:' +str(list))
list=list[:0]
print('List after deleting is:' +str(list))
