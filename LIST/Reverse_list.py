#using slicing technique
def reverse(list):
    new_lst=list[::-1]
    return new_lst
list=[12,34,65,77]
print(reverse(list))


#using by swapping present and last number at a time
def list_reverse(arr,size):
    if (size==1):
        return arr
    elif(size==2):
        arr[0], arr[1]=arr[1], arr[0]
        return arr
    else:
        for i in range(0,size//2):
            arr[i], arr[size-i-1]=arr[size-i-1],arr[i]
            if((i!=i+1 and size-i-1 != size-i-2) and (i!=size-i-2 and size-i-1!=i+1)):
               arr[i+1],arr[size-i-2]=arr[size-i-2],arr[i+1]
               i+=2
               return arr
arr=[1,2,3,4,5]
size=5
print('Original list:',arr)
print('Reversed list:',list_reverse(arr,size))


'''#using reversed() and reverse() Built-in function
list=[10,11,12,13,15,16]
list.reverse()
print('Using reverse()',list)
print("Using reversed() ", list(reversed(list)))

#using two_pointer Approach
def reverse_list(arr):
    left=0
    right=len(arr)-1
    while(left<right):
        temp=arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left+=1
        right-=1
    return arr
arr=[13,45,344,66,22]
print(reverse_list(arr))

#using insert()function
list=[10,11,12,13,14,15]
lst=[]
for i in list:
    lst.insert(0,i)
print(lst)'''

#using list comprehension
original_list=[10,12,13,14,15]
#new_list=[list[len(list)-1]for i in range(1,len(list)+1)]
new_list = [original_list[len(original_list) - i]
            for i in range(1, len(original_list)+1)]
print(new_list)
    
#using Numpy


import numpy as np
 
# Input list
my_list = [4, 5, 6, 7, 8, 9]
 
# Convert the list to a 1D numpy array
my_array = np.array(my_list)
 
# Reverse the order of the array
reversed_array = my_array[::-1]
 
# Convert the reversed array to a list
reversed_list = reversed_array.tolist()
 
# Print the reversed list
print(reversed_list)
