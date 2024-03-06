# list should be at least 2
list1 = [10, 20, 4, 45, 99]
 
mx = max(list1[0], list1[1]) 
secondmax = min(list1[0], list1[1]) 
n = len(list1)
for i in range(2,n): 
    if list1[i] > mx: 
        secondmax = mx
        mx = list1[i] 
    elif list1[i] > secondmax and \
        mx != list1[i]: 
        secondmax = list1[i]
    elif mx == secondmax and \
        secondmax != list1[i]:
          secondmax = list1[i]
 
print("Second highest number is : ",\
      str(secondmax))

#By removing maximum element from the list
list=[12,3,4,5,6,78]
new_lst=set(list)
new_lst.remove(max(new_lst))
print(max(new_lst))

#max list element on input provided by user
list=[23,4,20,98,45]
list.sort
n=len(list)
print('second largest element in the list:',list[n-1])

#using traversal
def findLargest(arr):
    secondLargest=0
    largest=min(arr)
    for i in range(len(arr)):
        if arr[i]>largest:
            secondLargest=largest
            largest=arr[i]
        else:
            secondLargest=max(secondLargest,arr[i])
    return secondLargest
arr=[10,23,45,67,98]
print(findLargest(arr))

#using list comprehension
def secondmax(arr):
    sublist=[x for x in arr if x<max(arr)]
    return max(sublist)
#if __name__=='__main__':
    arr=[10,20,4,45,99]
    print(secondmax(arr))

#using lambda function
lst=[12,20,34,53,6]
max1=max(lst)
max2=max(lst, key=lambda x: min(lst)-1 if (x==max1) else x)
print(max2)
