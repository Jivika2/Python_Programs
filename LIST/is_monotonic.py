def isMonotonic(A):
    x, y= [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x==A or y==A):
        return True
    return False
A=[6,5,4,4]
print(isMonotonic(A))
        
#
def isMonotonic(A):
    return(all(A[i]<=A[i+1] for i in range(len(A)-1))or
           all(A[i]>=A[i+1] for i in range(len(A)-1)))
A=[6,5,4,4]
print(isMonotonic(A))

#By checking length of array
def isMonotonic(arr):
    if len(arr)<=2:
        return True
    direction=arr[1]=arr[0]
    for i in range(2,len(arr)):
        if direction ==0:
            direction=arr[i]-arr[i-1]
            continue
        if (direction >0 and arr[i]<arr[i-1] or (direction<0 and arr[i]<arr[i-1])):
            return False
    return True
arr1=[1,2,3,4,5]
arr2=[5,15,20,10]
arr3=[2,4,5,6,7,8]
arr4=[1,2,3,4,5,6,7,8,9]
print(isMonotonic(arr1))
print(isMonotonic(arr2))
print(isMonotonic(arr3))
print(isMonotonic(arr4))
#
def is_monotonic(arr):
    unique_elements = set(arr)
    increasing = sorted(arr) == arr or sorted(arr, reverse=True) == arr
    return increasing
 
# Driver Code
arr1 = [6, 5, 4, 4]
arr2 = [5, 15, 20, 10]
arr3 = [2, 2, 2, 3]
 
print(is_monotonic(arr1))  
print(is_monotonic(arr2))  
print(is_monotonic(arr3))  
        
            
