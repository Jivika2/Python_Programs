# left_rotate Array
def reverse(start, end, arr):
    no_of_reverse=end-start+1
    count=0
    while(no_of_reverse)//2!=count:
        arr[start+count], arr[end-count]=arr[end-count],arr[start+count]
        count+=1
    return arr
def left_rotate_array(arr,size,d):
    start=0
    end=size-1
    arr=reverse(start,end,arr)
    start=size-d
    end=size-1
    arr=reverse(start,end,arr)
    return arr
arr=[1,2,3,4,5,6,7,8]
size=8
d=1
print('Original array:',arr)
if(d<=size):
    print('Rotated array:',left_rotate_array(arr,size,d))
else:
    d=d%size
    print('Rotated array:',left_rotate_array(arr,size,d))
#function to roted array by d elements using temp array
def rotateArray(arr,n,d):
    temp=[]
    i=0
    while(i<d):
        temp.append(arr[i])
        i=i+1
    i=0
    while(d<n):
        arr[i]=arr[d]
        i=i+1
        d=d+1
    arr[:]=arr[: i]+temp
    return arr
arr=[1,2,3,4,5,6,7,8]
print('Array after left rotation is:', end='')
print(rotateArray(arr,len(arr),2))

#using rotate one by one
def leftRotate(arr,d,n):
    for i in range(d):
        leftRotatebyOne(arr,n)
def leftRotatebyOne(arrr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
def printArray(arr,size):
    for i in range(size):
        print('%d'% arr[i],end='')
arr=[1,2,3,4,5,6,7,8]
leftRotate(arr,3,7)
printArray(arr,7)

#Using 4 juggling Algorithm
