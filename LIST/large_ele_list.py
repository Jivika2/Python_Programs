#using recursion
def findLargest(itr,ele,list1):
    if itr== len(list1):
        print('Largest element in the list is:',ele)
        return
    if ele<list1[itr]:
        ele=list1[itr]
    findLargest(itr+1,ele,list1)
    return
list1=[10,23,45,34,78]
findLargest(0,list1[0],list1)

#using heapq.nlargest()
import heapq
list=[12,34,68,578,567]
largest_ele=heapq.nlargest(1,list)[0]
print(largest_ele)
